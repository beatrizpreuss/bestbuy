
class Store:
    """A class to represent stores that contain products. Provides methods to
    add and remove products to the inventory, check products and quantity, and
    make an order"""

    def __init__(self, list_of_products):
        self.list_of_products = list_of_products


    def add_product(self, product):
        """Adds product to instance variable (list_of_products)"""
        self.list_of_products.append(product)


    def remove_product(self, product):
        """Removes product to instance variable (list_of_products)"""
        self.list_of_products.remove(product)


    def get_total_quantity(self):
        """Goes through list of products and returns the total
        quantity of products in the store"""
        total_products = []
        for product in self.list_of_products:
            if product.is_active():
                total_products.append(product.get_quantity())
        return sum(total_products)


    def get_all_products(self):
        """Goes through list of products, and returns a list with the
        active products (quantity > 0)"""
        active_products = []
        for product in self.list_of_products:
            if product.is_active():
                active_products.append(product)
        return active_products


    def order(self, shopping_list):
        """Receives a list of tuples as argument, calculates the prices for each
        quantity of product being ordered, and returns the total price of the order"""
        total_price = 0
        for product, quantity in shopping_list:
            if product.is_active():
                total_price += product.buy(quantity)
        return f"Order made! Total payment: ${total_price}"
