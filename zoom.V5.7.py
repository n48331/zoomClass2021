import time
import schedule
import os
import pyautogui as pi
import datetime
import calendar


# id & password (global)
passw = '057053'
id = '95576418008'

# main Fuction


def zoom(id, passw):
    os.startfile(r"Zoom.lnk")
    time.sleep(1)
    join = pi.locateCenterOnScreen('join.png', confidence=0.8)
    pi.click(join)
    time.sleep(1)
    pi.write(id, interval=0.02)
    time.sleep(1)

    join2 = pi.locateCenterOnScreen('join2.png', confidence=0.8)
    pi.click(join2)
    time.sleep(2)
    pi.write(passw, interval=0.02)
    time.sleep(1)

    join3 = pi.locateCenterOnScreen('join3.PNG', confidence=0.8)
    pi.click(join3)
    time.sleep(3)


def zoom1():
    zoom('2345678921', passw)


print("Started Schedules")
try:
    schedule.every().day.at("8:05").do(zoom1)
except:
    print("Some Error occurred on Class - 1")

try:
    schedule.every().day.at("9:00").do(zoom1)
except:
    print("Some Error occurred on Class - 2")

try:
    schedule.every().day.at("10:00").do(zoom1)
except:
    print("Some Error occurred on Class - 3")

try:
    schedule.every().day.at("11:00").do(zoom1)
except:
    print("Some Error occurred on Class - 4")

try:
    schedule.every().day.at("13:00").do(zoom1)
except:
    print("Some Error occurred on Class - 5")

day = datetime.datetime.today().weekday()
print(day)

week = calendar.day_name[day]
print(week)

while True:
    schedule.run_pending()
    time.sleep(1)
schedule.CancelJob()
