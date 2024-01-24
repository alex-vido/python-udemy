# https://docs.python.org/3.0/library/datetime.html
from datetime import datetime, timedelta

date = datetime(2022, 10, 27, 14, 49)
print(date)
print(date.strftime('%d/%m/%Y %H:%M:%S'))

date_1 = datetime.strptime("27/10/2022", "%d/%m/%Y")
print(date_1.strftime("%d/%m/%Y"))

print(date.timestamp())  # Is the seconds since 01-01-1970
date_2 = datetime.fromtimestamp(1666892940.0)
print(date_2)

date_1 = date_1 + timedelta(days=5)
print(date_1.strftime("%d/%m/%Y"))

d1 = date.strptime("27/10/2022", "%d/%m/%Y")
d2 = date.strptime("12/07/1993", "%d/%m/%Y")
dif = d1 - d2
print(dif)
print(d2 > d1)
