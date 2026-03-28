class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Electronics(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty


class Clothing(Product):
    def __init__(self, name, price, size, fabric):
        super().__init__(name, price)
        self.size = size
        self.fabric = fabric

class Wallet:
    def __init__(self):
        self.__balance = 0   # private

    def add_money(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    

class Product:
    def calculate_tax(self):
        pass


class Electronics(Product):
    def calculate_tax(self, price):
        return price * 0.15


class Clothing(Product):
    def calculate_tax(self, price):
        return price * 0.05


# usage
e = Electronics()
c = Clothing()

print("Electronics Tax:", e.calculate_tax(1000))
print("Clothing Tax:", c.calculate_tax(1000))