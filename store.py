import products

class Store:

    def __init__(self, list_of_products):
        self.list_of_products = list_of_products

    def add_product(self, product):
        self.list_of_products.append(product)

    def remove_product(self, product):
        self.list_of_products.remove(product)

    def get_total_quantity(self):
        total_products = 0
        for product in self.list_of_products:
            partial_quantity = product.quantity
            total_products += partial_quantity
        return total_products

    def get_all_products(self):
        active_products = []
        for product in self.list_of_products:
            if product.active:
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        total_price = 0
        for name, quantity in shopping_list:
            for product in self.list_of_products:
                if product == name and product.active:
                    partial_price = product.price * quantity
                    total_price += partial_price
        return f"Order cost: {total_price} dollars."


bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = products.Product("MacBook Air M2", price=1450, quantity=100)

# instance of a store
best_buy = Store([bose, mac])

pixel = products.Product("Google Pixel 7", price=500, quantity=250)
best_buy.add_product(pixel)

best_buy.order([(bose, 5), (mac, 30), (bose, 10)])