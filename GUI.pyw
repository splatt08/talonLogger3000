#! c:\\Users\\ipfa1\\AppData\\Local\\Programs\\Python\\Python310\\pythonw.exe
from talonLogger3000 import logger3000
import csv
import PySimpleGUI as sg

#grab logon data from csv
with open('logonList.csv', newline='') as logonList:
    for ac in csv.reader(logonList):
            logged_on_users = ac
#print("heyo test at call" + str(logged_on_users))


# setup GUI window
layout = [[sg.Text("enter a scan-id:  ")],
          [sg.Input(key='-INPUT-', do_not_clear=False)],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]
sg.theme('DarkGreen')
window = sg.Window('Talon Logger 3000', layout, size=(1080, 720), finalize=False)


running = True
while running:
    event, values = window.read()
    # Grab values from scanner
    #print("heyo test at before func call" + str(logged_on_users))
    scan_num = values['-INPUT-'] # numerical value from scanner (hopefully an int)
    #print("heyo test after func call" + str(logged_on_users))
    if scan_num == "STOP" or event == sg.WINDOW_CLOSED or event == 'Quit':
        running = False
        continue
    else:
        logger_data = logger3000(scan_num, logged_on_users)
        logged_on_users = logger_data[5]
    if logger_data[1] != 'null':
        window['-OUTPUT-'].update('')
        if logger_data[4] == "True":
            window['-OUTPUT-'].update(logger_data[0] + ' has been signed in')
        else:
            window['-OUTPUT-'].update(logger_data[0] + ' has been signed out')
    else:
        window['-OUTPUT-'].update('ERROR!')


window.close()