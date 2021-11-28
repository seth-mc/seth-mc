import pyautogui
import openpyxl as xl
import time
from threading import Thread
from pynput import keyboard
from pynput.mouse import Listener
import os
import re


def exit_program():  # makes escape key an actual thing
    def on_press(key):
        if str(key) == 'Key.esc':
            main.status = 'pause'
            user_input = input(
                'Program paused, would you like to continue? (y/n) ')

            while user_input != 'y' and user_input != 'n':
                user_input = input('Incorrect input, try either "y" or "n" ')

            if user_input == 'y':
                main.status = 'run'
            elif user_input == 'n':
                main.status = 'exit'
                exit()

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


def mouse_iterator():
    def on_click(button):
        main.status = 'run'
        if not pressed:
            # Stop listener
            return False

    # Collect events until released
    with Listener(on_click=on_click) as listener2:
        listener2.join()


def main():  # the main program
    main.status = 'run'

    while True:
        print('running')
        time.sleep(1)

        while main.status == 'pause':
            time.sleep(1)

        if main.status == 'exit':
            print('Main program closing')
            break

# simutaneously start running pyautogui (main) and escape key 'sensor' (exit_program)

Thread(target=main).start()
Thread(target=exit_program).start()
