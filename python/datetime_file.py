from datetime import datetime

x = datetime.now()

print(x)

new_date = datetime.now()

print(new_date)

print(new_date.strftime("%B"))

x = datetime(year=2023, month= 12, day= 12, hour= 10, minute=24)

print(x)

x = datetime(day= 12, month= 12, year= 2024)

print(x)

x = datetime.now()

print(x.strftime("%x"))

print(x.strftime("%A, %d %B %Y, %H:%M:%S"))