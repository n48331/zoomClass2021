import datetime
import calendar

day = datetime.datetime.today().weekday()
print(day)

week = calendar.day_name[day]
print(week)

fivep = [0, 1, 3, 5]
fourp = [2, 4]
