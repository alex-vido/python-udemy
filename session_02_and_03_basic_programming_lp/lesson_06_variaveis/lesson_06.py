"""

IMC	CLASSIFICAÇÃO	OBESIDADE (GRAU)
MENOR QUE 18,5	MAGREZA	0
ENTRE 18,5 E 24,9	NORMAL	0
ENTRE 25,0 E 29,9	SOBREPESO	I
ENTRE 30,0 E 39,9	OBESIDADE	II
MAIOR QUE 40,0	OBESIDADE GRAVE	III

"""

nome = 'Alex Vido'
idade = 29
altura = 1.64
peso = 78
e_maior = idade > 18
data1 = True
data_atual = 2022
imc = peso / (altura ** 2)

print(nome, "tem", idade, "anos de idade, e seu imc é:", imc)
