# Some valores com list comprehesion

carrinho = []
carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))
n = 0
total = sum([y for x, y in carrinho])
# total = sum([x[1] for x in carrinho])  # São iguais
print(f'{carrinho} [Total R${total}]')
