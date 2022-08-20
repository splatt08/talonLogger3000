import os
import sys
import csv
import datetime




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


