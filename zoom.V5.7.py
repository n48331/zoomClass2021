import time
import schedule
import os
import pyautogui as pi
import datetime
import calendar


# id & password (global)
passw = '057053'
id = '95576418008'

fivep = [0, 1, 3, 5]
fourp = [2, 4]

# 0-mon,1-tue,2-wed,3-thu,4-fri,5-sat,6-sun
day = datetime.datetime.today().weekday()
print(day)

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


week = calendar.day_name[day].upper()
print("Started Schedules for {}".format(week))

try:
    schedule.every().day.at("08:05").do(zoom1)
except:
    print("Some Error occurred on Class - 1")

try:
    schedule.every().day.at("09:00").do(zoom1)
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


while True:
    schedule.run_pending()
    time.sleep(1)
schedule.CancelJob()
