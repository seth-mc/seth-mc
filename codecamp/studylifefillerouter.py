import pyautogui
import time
import pandas as pd
import datetime as dt
from pynput import keyboard
from threading import Thread


def exit_program():
    def on_press(key):
        if str(key) == 'Key.f1':

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


def main():
    main.status = 'run'
    while True:

        data = pd.read_excel('/Users/seth/Desktop/Due Dates.xlsx', headers=0)
        data.columns = ['a', 'b', 'c', 'd', 'e']
        data['c'] = data['c'].dt.strftime('%B %-d %Y')
        data['c'] = data['c'].str.lower()
        #data['d'] = data['d'].str.lower()
        #data['e'] = data['e'].str.lower()
        time.sleep(10)
        print("startin' er up!")
        for row in data.itertuples():
            # coordinates
            new = [968, 489]
            opensubject = [878, 346]
            subject = {'Corporate Finance - COM 445': [818, 365], 'Strategic Management - COM 400': [771, 433], 'Taxation for Managers - COM 425': [
                845, 457], 'Legal Issues in Management - COM 402': [798, 392], 'Management Accounting II - COM 426': [866, 410], 'Career Preparation Across Borders - COM 405': [878, 346]}
            opentyper = [1081, 339]
            typer = {'Assignment': [1055, 350], 'Reminder': [1107, 341]}
            duedate = [743, 429]
            title = [786, 510]
            detail = [821, 593]
            save = [1223, 721]

            pyautogui.keyDown('shift')
            pyautogui.keyUp('shift')

            # Subject
            pyautogui.click(new[0], new[1])
            time.sleep(1)
            pyautogui.click(opensubject[0], opensubject[1])
            time.sleep(1)
            for key in subject.keys():
                if key in row[1]:
                    x = subject.get(key)
                    pyautogui.click(x[0], x[1])
                    time.sleep(1)
            pyautogui.click(opentyper[0], opentyper[1])
            time.sleep(1)

            # Type
            for key in typer.keys():
                if key in row[2]:
                    x = typer.get(key)
                    pyautogui.click(x[0], x[1])

            # Date
            pyautogui.doubleClick(duedate[0], duedate[1])
            pyautogui.hotkey('command', 'a')
            pyautogui.click(duedate[0], duedate[1])

            time.sleep(1)
            pyautogui.keyUp('shift')
            pyautogui.write(row[3], interval=0.05)
            pyautogui.click(1104, 422)
            time.sleep(0.5)

            # Title
            pyautogui.click(title[0], title[1])
            time.sleep(1)
            pyautogui.keyUp('shift')
            pyautogui.write(row[4], interval=0.05)
            time.sleep(0.5)

            # Detail
            pyautogui.click(detail[0], detail[1])
            pyautogui.keyUp('shift')
            pyautogui.write(row[5], interval=0.01)
            time.sleep(0.5)

            pyautogui.click(save[0], save[1])
            time.sleep(2.5)
        
        print('done!')
        break
        while main.status == 'pause':
            time.sleep(1)

        if main.status == 'exit':
            print('Main program closing')
            break


Thread(target=main).start()
Thread(target=exit_program).start()
