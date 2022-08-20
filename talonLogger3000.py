import os
import sys
import csv
import datetime
import PySimpleGUI as sg

#grab logon data from csv
with open('logonList.csv', newline='') as logonList:
    for ac in csv.reader(logonList):
            logged_on_users = ac
#print("heyo test at call" + str(logged_on_users))

# logger3000 is the function that finds, sorts, and records with scanner number as input (and the logged_on_user list)
def logger3000(_scan_num, _logged_on_users):
    #print("heyo test in func" + str(_logged_on_users))
    #variables
    name = ''
    write = False

    # Grab data from users csv file
    with open('users.csv', newline='') as users_csv:
        user_read = csv.reader(users_csv)

        for row in user_read:
        
            if row[1] == _scan_num:
                name = row[0]
                write = True

    if write:
        # check if user logged 
        if name in _logged_on_users:
            _logged_on_users.remove(name)
            logon = 'False'
        else:
            _logged_on_users.append(name)
            logon = 'True'
        with open('logonList.csv', 'w',  newline='') as logonList:
            csv.writer(logonList).writerow(_logged_on_users)
        #print("heyo test at list write" + str(_logged_on_users))

        # grab time and date
        t = datetime.datetime.now()
        time = str(t.hour) + ':' + str(t.minute) + ':' + str(t.second)
        date = str(t.month) + '/' + str(t.day) + '/' + str(t.year)

        # write data to log csv file
        with open('log.csv', 'a+', newline='') as log_csv:
            csv.writer(log_csv).writerow([name, _scan_num, time, date, logon])
        return([name, _scan_num, time, date, logon, _logged_on_users])

    else:
        
        return(["null", "null", "null", "null", "null", _logged_on_users])

# setup GUI window
layout = [[sg.Text("enter a scan-id:  ")],
          [sg.Input(key='-INPUT-', do_not_clear=False)],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]
sg.theme('DarkGreen')
window = sg.Window('Talon Logger 3000', layout, size=(1080, 720), finalize=True)


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



