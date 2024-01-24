from functools import reduce
from session_03_py_intermediary_procedural.lesson_60_reduce.lesson_58_dados import pessoas, produtos, lista

sum_list = reduce(lambda ac, i: i + ac, lista, 0)
print(sum_list)

print('\n', '#' * 120, '\n')

sum_products = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(sum_products)
print(round(sum_products / (len(produtos))))

print('\n', '#' * 120, '\n')

sum_years = reduce(lambda ac, y: y['idade'] + ac, pessoas, 0)
print(sum_years)
print(round(sum_years / len(pessoas)))
