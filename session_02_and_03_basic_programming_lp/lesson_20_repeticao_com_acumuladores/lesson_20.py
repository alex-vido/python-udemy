"""

While/Else
Contadores
Acumuladores

"""

contador = 1
acumulador = 1

print(contador, acumulador)

while contador <= 100:
    # print(contador, acumulador)  # print aqui não mostrará o último resultado

    if contador > 5:  # Não passará pelo else
        break

    acumulador += contador
    contador += 1

    print(contador, acumulador)  # Print aqui não mostrará o primeiro resultado

# else:
#    print('Cheguei no else')
print('Acabou')
