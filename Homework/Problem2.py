#Task1:
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price}")

#Task2 & Task3:
class Book(Product):
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)
        self.author = author

    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}")
    
class Electronic(Product):
    def __init__(self, product_id, name, price, specs):
        super().__init__(product_id, name, price)
        self.specs = specs

    def display_info(self):
        super().display_info()
        print(f"Specs: {self.specs}")

class Clothing(Product):
    def __init__(self, product_id, name, price, size):
        super().__init__(product_id, name, price)
        self.size = size

    def display_info(self):
        super().display_info()
        print(f"Size: {self.size}")

#Task4:


book = Book("B001", "The Great Gatsby", 10.99, "F. Scott Fitzgerald")
electronic = Electronic("E001", "Smartphone", 999.99, "128GB, Black, Unlocked")
clothing = Clothing("C001", "T-Shirt", 19.99, "Medium")


book.display_info()
electronic.display_info()
clothing.display_info()

