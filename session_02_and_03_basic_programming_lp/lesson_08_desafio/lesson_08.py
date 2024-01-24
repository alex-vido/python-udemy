"""
* Criar variaveis para nome (str), idade (int)
* Altura (float) e peso (float) de uma pessoa
* Criar variavel com ano atual (int)
* Obter o ano de nascimento da pessoa (Baseado na idade e ano atual)
* Obter imc com 2 casas decimais
* Mostrar todos os valores com na tela com F-Strings
"""
nome = "Alex"
idade = 29
altura = 1.64
peso = 85.5
ano_atual = 2022
ano_nascimento = ano_atual - idade
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos, nasceu em {ano_nascimento}')
print(f'{nome} pesa {peso} e seu IMC é {imc:.2f}')
