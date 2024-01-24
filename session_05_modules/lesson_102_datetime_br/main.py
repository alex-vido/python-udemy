from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays, monthrange


setlocale(LC_ALL, 'pt_BR.utf-8')

dt = datetime.now()
format_1 = dt.strftime('%A, %d de %B de %Y')
format_2 = dt.strftime('%d/%m/%Y %H:%M:%S')
print(format_1)
print(format_2)

actual_month = int(dt.strftime('%m'))
print(mdays)  # May fail in bisix years, not consider the 0

print(actual_month, mdays[actual_month])

# Day of week. Sunday 0, Monday 1...
print(monthrange(2022, 2))
day_week, last_day = monthrange(2022, 2)
print(last_day)

last_days_of_months_actual_year = [
    monthrange(datetime.now().year, mes)[1] for mes in range(1, 13)
]
print(last_days_of_months_actual_year)
