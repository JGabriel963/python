class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discount(self, value):
        new_price = self.price - (self.price * (value / 100))
        return new_price

    def __str__(self):
        return f"Nome: {self.name} \nPreço: {self.price}"


xbox = Product("Xbox One", 4000)
print(xbox)
print(xbox.discount(20))
iphone = Product("Iphone 14", 8000)
print(iphone)
print(iphone.discount(10))
