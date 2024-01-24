class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        for product in self.products:
            print(product.name, product.price)

    def sum_total(self):
        total = 0
        for product in self.products:
            total += product.price
        return f'O total da sua compra é: R$ {total:.2f}'


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
