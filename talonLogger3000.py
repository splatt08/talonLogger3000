import os
import sys
import csv
import datetime


# Grab values from scanner
scan_num = '1234' # numerical value from scanner (hopefully an int)


# find, sort, and record with scanner number
# scan for a matching user

#grab logon data from csv
with open('logonList.csv', newline='') as logonList:
    for ac in csv.reader(logonList):
            logged_on_users = ac
#variables
name = ''
write = False



# Grab data from users csv file
with open('users.csv', newline='') as users_csv:
    user_read = csv.reader(users_csv)

    for row in user_read:
        
        if row[1] == scan_num:
            name = row[0]
            write = True
            


if write:
    # check if user logged 
    if name in logged_on_users:
        logged_on_users.remove(name)
        logon = 'False'
    else:
        logged_on_users.append(name)
        logon = 'True'
    with open('logonList.csv', 'w',  newline='') as logonList:
        csv.writer(logonList).writerow(logged_on_users)

    # grab time and date
    t = datetime.datetime.now()
    time = str(t.hour) + ':' + str(t.minute) + ':' + str(t.second)
    date = str(t.month) + '/' + str(t.day) + '/' + str(t.year)

    # write data to log csv file
    with open('log.csv', 'a+', newline='') as log_csv:
        csv.writer(log_csv).writerow([name, scan_num, time, date, logon])

else:
    print('Error!')
