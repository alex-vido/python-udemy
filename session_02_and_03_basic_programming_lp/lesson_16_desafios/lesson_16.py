# Desafio 1. Usuário digitar número, informar se é par ou ímpar, ou se não é inteiro

numero = input("Digite um número: ")

if not numero.isnumeric():
    print("Número não inteiro")

else:
    numero = int(numero)

    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")


# Desafio 2. Perguntar hora, e informar bom dia, boa tarde ou boa noite, de acordo com o horário.

horas = input("Digite o horário (0-23): ")

if horas.isnumeric():
    horas = int(horas)

    if horas < 0 or horas > 24:
        print("O horário deve estar entre 0 e 23.")
    else:
        if horas <= 11:
            print("Bom dia!")
        elif horas <= 17:
            print("Boa tarde!")
        else:
            print("Boa noite!")

else:
    print("Digite um horário entre 0 e 23.")


# Desafio 3. Perguntar 1 nome. Se nome for menor ou igual a 4 informar pequeno. Até 6 normal e maior muito grande.

nome = input("Digite o seu nome: ")
if len(nome) <= 4:
    print("Seu nome é muito curto")
elif len(nome) <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")
