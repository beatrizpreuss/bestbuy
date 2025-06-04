import products
import store

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)


def start(store_name):
    while True:
        try:
            print("\n------- Store Menu -------\n"
                  "1. List all products in store\n"
                  "2. Show total amount in store\n"
                  "3. Make an order\n"
                  "4. Quit")
            user_choice = int(input("Please choose a number: "))
            print("---------------------------\n")

            if user_choice == 1:
                counter = 1
                for product in store_name.get_all_products():
                    print(f"{counter}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")
                    counter += 1

            elif user_choice == 2:
                total_amount = store_name.get_total_quantity()
                print(f"Total of {total_amount} items in store")

            elif user_choice == 3:
                shopping_list = []
                counter = 1
                for product in store_name.get_all_products():
                    print(f"{counter}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")
                    counter += 1

                print("\nWhen you want to finish your order, enter empty text.\n")

                while True:
                    product_choice = input("What product # do you want? ")
                    quantity_choice = input("What amount do you want? ")
                    print("")
                    if product_choice == "" and quantity_choice == "":
                        break
                    shopping_list.append((product_list[int(product_choice) - 1], int(quantity_choice)))
                print(store_name.order(shopping_list))

            elif user_choice == 4:
                break

            else:
                print("Invalid number, try again")

        except ValueError:
            print("\nInvalid input, try again")


if __name__ == "__main__":
    start(best_buy)