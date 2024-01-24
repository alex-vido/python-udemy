"""

Manipulação de Strings
* Strings Indices
* Fatiamento de Strings
* Funções Built-in len, abs, type, print, etc...
Essas funções podem ser utilizadas dirertamente em cada tipo.

"""

texto = 'Python S2'
nova_string = texto[2:6]  # O array 6 não é incluido
url = 'www.google.com.br/'

# Positivos
print(texto[2])  # t

# Negativos
print(texto[-4])

print(url[:-1])  # Barra / removida
print(nova_string)
print(texto[:6])  # Pegará do indice 0 até o 5
print(texto[7:])  # Pegará do indice 6 até o final
print(texto[-9:-3])  # Pegará do indice -9 (que nessa var é o indice 0, até o -4)
print(texto[0::2])  # Começará do indice 0, e pulará de 2 em 2, nesse caso: Pto 2
print(texto[0:6:2])  # Começará do indice 0 até o 5, e pulará de 2 em 2, nesse caso: Pto 2

for letra in texto:
    print(letra)
