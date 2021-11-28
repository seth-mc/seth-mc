import warnings

# filter updated python warning
warnings.filterwarnings("ignore", category=UserWarning)

import time
from threading import Thread
from pynput import keyboard
from pynput.mouse import Listener
import os
import sys
import re
import pyperclip


def program():  
    def on_press(key):

        if str(key) == 'Key.esc':  # makes escape key an actual thing
            main.status = 'pause'
            user_input = input('\nProgram paused, would you like to continue? (y/n) ')
            while True:
                if user_input == 'y':
                    main.status = 'run'
                elif user_input == 'n':
                    main.status = 'exit'
                    exit()
                else:
                    user_input = input('Incorrect input, try either "y" or "n" ')


        if 'char' in dir(key):  # looks for the "v" key being pressed
            if key.char == 'v':
                try:
                    pyperclip.copy(allstuff[0])  # copies first list item
                    print("", end="\n{} Items Left.".format(len(allstuff) - 1))
                    allstuff.pop(0)  # pops first list item
                except IndexError:  # occurs when you run out of things to paste
                    user_input = input(
                        '\nProgram paused, would you like to continue? (y/n) ')
                    while True:
                        if user_input == 'y':
                            main.status = 'run'
                        elif user_input == 'n':
                            main.status = 'exit'
                            exit()
                        else:
                            user_input = input('Incorrect input, try either "y" or "n" ')



    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


def main():  # the 'heart' (main) of the program
    main.status = 'run'

    while True:
        time.sleep(1)

        while main.status == 'pause':
            time.sleep(1)

        if main.status == 'exit':
            print('Main program closing')
            break

print('\nRAW:')  # user input that accepts multilines
lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
raw = '\n'.join(lines)



user_input = input('Want to split or REGEX? \n')  # two options
while True:
    if user_input.lower() == 'regex':  # REGEX: finds it using your inputted regex formula
        regex = input('REGEX formula: \n')
        stuff = re.compile(r'{}'.format(regex))
        allstuff = stuff.findall(raw)
        if not allstuff:
            print("ERROR: Nothing Found.")
        else:
            pyperclip.copy(allstuff[0])
        break

    elif user_input.lower() == 'split':  # SPLIT: splits all items by common character
        sep = input('SEPARTOR: \n')
        allstuff = raw.split(sep)
        pyperclip.copy(allstuff[0])
        break
    else:
        user_input = input('Incorrect input, try either "split" or "regex" ')
        continue
    

Thread(target=main).start()
Thread(target=program).start()




