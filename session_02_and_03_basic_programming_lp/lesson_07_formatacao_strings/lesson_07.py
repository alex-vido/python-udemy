nome = 'Alex Vido'
idade = 29
altura = 1.64
peso = 78
e_maior = idade > 18
data1 = True
data_atual = 2022
imc = peso / (altura ** 2)

print(nome, "tem", idade, "anos de idade, e seu imc é:", imc)
print(f'{nome} tem {idade} anos de idade, e seu imc é: {imc:.2f}')
print('{} tem {} anos de idade, e seu imc é: {:.2f}'.format(nome, idade, imc))
print('{0} tem {1} anos, e seu imc é: {2:.2f}\
 {0} tem {3} de altura'.format(nome, idade, imc, altura))
print('{n} tem {i} anos, seu imc é: {im:.2f}'.format(n=nome, i=idade, im=imc))
