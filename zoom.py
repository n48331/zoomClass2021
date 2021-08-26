
import time
import schedule
import os
import pyautogui as pi
import datetime
import calendar
from keyboard import press

os.startfile(r"assets\Zoom.lnk")
# id & password (global)
passw = '057053'
id = '95576418008'
times = ["08:05", "09:00", "10:00", "11:00", "13:00"]

print('id : '+id, 'password : '+passw)
# 0-mon,1-tue,2-wed,3-thu,4-fri,5-sat,6-sun
day = datetime.datetime.today().weekday()


if day == 0 or day == 1 or day == 3 or day == 5:
    times.pop()
    if day == 0:
        times.pop(1)
elif day == 2:
    times.pop(1)

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
if day == 6:
    print("Its Holiday, No classes Today, Sleep Well 😃")
elif day == 2 or day == 4:
    print("Started Schedules for {}. 5 classes".format(week))
else:
    print("Started Schedules for {}. 4 classes".format(week))

for x in times:
    if day == 6:
        break
    else:
        try:
            schedule.every().day.at(x).do(zoom1)
            print("class for today at {} scheduled...✅".format(x))
        except:
            print("Some Error occurred on Class - {}".format(x))


while True:
    schedule.run_pending()
    time.sleep(1)
schedule.CancelJob()
