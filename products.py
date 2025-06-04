
class Product:
    """A class to represent products. Provides methods to get and set quantity,
    check if active, activate and deactivate, and buy product"""

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

        if name == "":
            raise Exception("Please name your product")
        elif price < 0:
            raise Exception("Price cannot be negative")
        elif quantity < 0:
            raise Exception("Quantity cannot be negative")


    def get_quantity(self):
        """Returns the current quantity of the product"""
        return self.quantity


    def set_quantity(self, quantity):
        """Sets product quantity for the instance variable"""
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()
        else:
            self.activate()


    def is_active(self):
        """Checks the instance variable (active)"""
        if self.active:
            return True
        else:
            return False


    def activate(self):
        """Changes instance variable (active) to True"""
        self.active = True


    def deactivate(self):
        """Changes instance variable (active) to False"""
        self.active = False


    def show(self):
        """Prints product info"""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")


    def buy(self, quantity):
        """Buys a given quantity of the product.
        Returns the total price of the purchase.
        Updates the quantity of the product"""
        if quantity <= 0:
            raise Exception("Please choose valid quantity")
        elif quantity > self.quantity:
            raise Exception(f"Unfortunately, there are only {self.quantity} {self.name}s in the store")
        total_price = quantity * self.price
        self.set_quantity(self.quantity - quantity)
        return total_price
