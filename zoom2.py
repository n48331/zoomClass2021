import time
import schedule
import os
import pyautogui as pi
import datetime
import calendar
from keyboard import press

# id & password (global)
passw = '057053'
id = '95576418008'
times = ["08:05", "09:00", "10:00", "11:00", "12:00"]

tt = [[1, 0, 1, 1, 0],
      [1, 1, 1, 1, 0],
      [1, 0, 1, 1, 1],
      [0, 0, 1, 1, 0],
      [1, 1, 1, 1, 1],
      [1, 1, 1, 1, 0]]

os.startfile(r"assets\Zoom.lnk")

print('id : '+id, 'password : '+passw)
# 0-mon,1-tue,2-wed,3-thu,4-fri,5-sat,6-sun
day = datetime.datetime.today().weekday()

# main Fuction


def zoom(id, passw):
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    try:
        os.startfile(r"assets\Zoom.lnk")
        time.sleep(1)
        join = pi.locateCenterOnScreen('assets\icons\join.png', confidence=0.8)
        pi.click(join)
        time.sleep(2)
        pi.write(id, interval=0.05)
        press('enter')
        time.sleep(2)
        pi.write(passw, interval=0.05)
        press('enter')
        print("Class Started from {}".format(current_time))
    except:
        print("Not Done.Some ERROR occurred ! ! !")


def zoom1():
    zoom(id, passw)


week = calendar.day_name[day].upper()
if day != 6:
    count = tt[day].count(1)

if day == 6:
    print("Its Holiday, No classes Today, Sleep Well 😃")
elif day != 6:
    print('day : {}'.format(week))
    print('Periods : {}'.format(count))
    for i in range(len(tt[0])):
        if tt[day][i]:
            try:
                schedule.every().day.at(times[i]).do(zoom1)
                print("class for today at {} scheduled...✅".format(times[i]))
            except:
                print(
                    "Some Error occurred on Class - {}".format(i))

while True:
    schedule.run_pending()
    time.sleep(1)
schedule.CancelJob()
