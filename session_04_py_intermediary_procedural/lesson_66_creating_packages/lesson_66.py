
from sales.lesson_66_calc_prices import increase, decrease

price = 49.90
price_increase = increase(price, 15, format_value=True)
price_decrease = decrease(price, 10, format_value=True)

print(price_increase)
print(price_decrease)
