import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import time
import threading
from pynput import keyboard
import re
import pyperclip
from queue import Queue

class ClipboardManager:
    def __init__(self):
        self.allstuff = []
        self.status = 'run'
        self.command_queue = Queue()
        self.lock = threading.Lock()
    
    def on_press(self, key):
        if key == keyboard.Key.esc:
            self.command_queue.put('pause')
            return False  # Stop listener
        
        if hasattr(key, 'char') and key.char == 'v':
            with self.lock:
                if self.allstuff:
                    pyperclip.copy(self.allstuff[0])
                    print(f"\n{len(self.allstuff) - 1} Items Left.", end='', flush=True)
                    self.allstuff.pop(0)
                else:
                    print("\nNo more items to paste!", flush=True)
                    self.command_queue.put('empty')
                    return False  # Stop listener
    
    def start_listener(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()
    
    def run(self):
        # Get user input first
        print('\nRAW:')
        lines = []
        while True:
            line = input()
            if line:
                lines.append(line)
            else:
                break
        raw = '\n'.join(lines)
        
        # Process input
        while True:
            user_input = input('Want to split or REGEX? \n').lower()
            if user_input == 'regex':
                regex = input('REGEX formula: \n')
                pattern = re.compile(regex)
                self.allstuff = pattern.findall(raw)
                if not self.allstuff:
                    print("ERROR: Nothing Found.")
                    return
                break
            elif user_input == 'split':
                sep = input('SEPARATOR: \n')
                self.allstuff = raw.split(sep)
                break
            else:
                print('Incorrect input, try either "split" or "regex"')
        
        # Copy first item
        with self.lock:
            if self.allstuff:
                pyperclip.copy(self.allstuff[0])
                print(f"Ready! {len(self.allstuff)} items loaded.")
        
        # Main loop
        while self.status == 'run':
            # Start keyboard listener in a separate thread
            listener_thread = threading.Thread(target=self.start_listener)
            listener_thread.start()
            listener_thread.join()  # Wait for listener to finish
            
            # Check if we need to handle commands
            if not self.command_queue.empty():
                command = self.command_queue.get()
                
                if command == 'pause':
                    user_input = input('\nProgram paused, would you like to continue? (y/n) ')
                    if user_input.lower() == 'n':
                        self.status = 'exit'
                        break
                    # If 'y', restart the listener
                    
                elif command == 'empty':
                    user_input = input('\nNo more items. Add more items? (y/n) ')
                    if user_input.lower() == 'n':
                        self.status = 'exit'
                        break
                    elif user_input.lower() == 'y':
                        # Allow adding more items
                        print('\nAdd more items (empty line to finish):')
                        lines = []
                        while True:
                            line = input()
                            if line:
                                lines.append(line)
                            else:
                                break
                        if lines:
                            new_raw = '\n'.join(lines)
                            # Use the same processing method as before
                            # You might want to remember the last used method
                            with self.lock:
                                self.allstuff.extend(new_raw.split('\n'))
                            print(f"Added {len(lines)} new items.")

if __name__ == "__main__":
    manager = ClipboardManager()
    manager.run()
