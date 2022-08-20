import os
import sys
import csv
import datetime


# Grab values from scanner
scan_num = '1234' # numerical value from scanner (hopefully an int)


# find, sort, and record with scanner number
# scan for a matching user

#variables
name = 'a'
write = False

# Grab data from users csv file
with open('users.csv', newline='') as users_csv:
    user_read = csv.reader(users_csv)

    for row in user_read:
        
        if row[1] == scan_num:
            name = row[0]
            write = True
            


if write:
    # grab time and date
    t = datetime.datetime.now()
    time = str(t.hour) + ':' + str(t.minute) + ':' + str(t.second)
    date = str(t.month) + '/' + str(t.day) + '/' + str(t.year)

    # write data to log csv file
    with open('log.csv', 'a+', newline='') as log_csv:
        csv.writer(log_csv).writerow([name, scan_num, time, date])

else:
    print('Error!')
