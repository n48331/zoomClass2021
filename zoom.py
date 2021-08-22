import time
import schedule
import os
import pyautogui as pi
import datetime
import calendar


# id & password (global)
passw = '057053kl'
id = '95576418008'
times = ["22:40", "09:00", "10:00", "11:00", "13:00"]

# 0-mon,1-tue,2-wed,3-thu,4-fri,5-sat,6-sun
day = datetime.datetime.today().weekday()
if day == 2 or day == 4:
    times.pop()

# main Fuction


def zoom(id, passw):
    os.startfile(r"assets\Zoom.lnk")
    time.sleep(1)
    join = pi.locateCenterOnScreen('assets\icons\join.png', confidence=0.8)
    pi.click(join)
    time.sleep(1)
    pi.write(id, interval=0.05)
    time.sleep(1)

    join2 = pi.locateCenterOnScreen('assets\icons\join2.PNG', confidence=0.8)
    pi.click(join2)
    time.sleep(2)
    pi.write(passw, interval=0.05)
    time.sleep(1)

    join3 = pi.locateCenterOnScreen('assets\icons\join3.PNG', confidence=0.8)
    pi.click(join3)
    time.sleep(3)
    print("Done..❌")


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
        exit()
    else:
        try:
            schedule.every().day.at(x).do(zoom1)
            print("class for today at {} scheduled...✅".format(x))
        except:
            print("Some Error occurred on Class - {}".format(index(x)))


while True:
    schedule.run_pending()
    time.sleep(1)
schedule.CancelJob()
