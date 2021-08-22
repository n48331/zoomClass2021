import time
import schedule
import os
import pyautogui as pi

passw = '057053'
id = '95576418008'


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
    schedule.every().day.at("19:10").do(zoom1)

except:
    print("Some Error Occured")


while True:
    schedule.run_pending()
    time.sleep(1)
schedule.CancelJob()
