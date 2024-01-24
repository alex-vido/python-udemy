from classes import Cart, Product

carrinho = Cart()
p1 = Product('T-Shirt', 50)
p2 = Product('iPhone', 10000)
p3 = Product('Mug', 25)

carrinho.add_product(p1)
carrinho.add_product(p2)
carrinho.add_product(p3)

carrinho.list_products()
print(carrinho.sum_total())
