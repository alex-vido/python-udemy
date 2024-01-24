"""

+      Soma
-      Subt
*      Multp
/      Divisão
//     Divisão inteira
**     Elevação
%      Resto
()     Alterar precedência


Abaixo, segue uma lista mais precisa de quais operadores
tem maior prioridade na hora de realizar contas mais complexas
 (de maior para menor precedência).

    ( n + n ) - Os parênteses têm a maior precedência,
    contas dentro deles são realizadas primeiro

    ** - Depois vem a exponenciação

    * / //  % - Na sequência multiplicação, divisão, divisão inteira e módulo

    +  - - Por fim, soma e subtração

"""

print("Multiplicação * ", 10 * 10)
print("Adição +", 10 + 10)
print("Subtração - ", 10 - 10)
print("Divisão / ", 10 / 3)
print("Divisão inteira // ", 10 // 3)
print("Resto divisão % ", 10 % 3)
print("Multiplicação", 10 * 'Alex ')
print("Presedência ()", (5+2) * 10)
