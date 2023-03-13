# arquivo: user.py

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.addresses = []
        self.orders = []

    def add_address(self, address):
        self.addresses.append(address)

    def add_order(self, order):
        self.orders.append(order)


# arquivo: address.py

class Address:
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code


# arquivo: order.py

class Order:
    def __init__(self, user, products, payment_method):
        self.user = user
        self.products = products
        self.payment_method = payment_method
        self.total_price = 0

    def calculate_total_price(self):
        for product in self.products:
            self.total_price += product.price

