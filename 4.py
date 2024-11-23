import time
from datetime import datetime

# Поточна дата та час
current_time = datetime.now()

# Виведення у різних форматах
print("Current date and time:", current_time)
print("Current year:", current_time.year)
print("Month of year:", current_time.strftime("%B"))
print("Week number of the year:", current_time.strftime("%U"))
print("Weekday of the week:", current_time.weekday() + 1)
print("Day of year:", current_time.timetuple().tm_yday)
print("Day of the month:", current_time.day)
print("Day of week:", current_time.strftime("%A"))
