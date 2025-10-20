import products
import store
import textwrap
from termcolor import colored


def products_list(best_buy):
    """"Lists all products in store."""
    active_products = best_buy.get_all_products()
    for index, product in enumerate(active_products):
        print(f"{index+1}. ", end="")
        product.show()

    return active_products


def products_quantity(best_buy):
    """Shows total amount in store."""
    total_amount = best_buy.get_total_quantity()
    print(f"Total of {total_amount} items in store")


def shopping_cart(best_buy):
    """Creates a shopping list"""
    print("When you want to finish order, enter empty text.\n")
    shopping_list = []
    active_products = products_list(best_buy)

    while True:
        product_num = input("\nWhich product # do you want? ")
        if product_num == "":
            break
        try:
            product_num = int(product_num)
        except ValueError:
            print("Please enter a valid product number or empty to finish.")
            continue
        if product_num < 1 or product_num > len(active_products):
            print("Invalid product number.")
            continue

        amount = int(input("What amount do you want? "))
        if amount <= 0:
            print("Amount must be > 0.")
            continue

        shopping_list.append((active_products[product_num-1],amount))
        print(colored("Product added to list!",'green'))

    print(colored("\nOrder made!\n",'yellow'))
    for product,amount in shopping_list:
        print(f"- {product.name}, {amount} items, price: {product.price*amount}")
    total_price = best_buy.order(shopping_list)
    print("\n"+"*"*35)
    print(colored("Total payment:",'blue'), colored(total_price,'blue'))


def start(best_buy):
    """Calls shop menu."""
    while True:
        print(textwrap.dedent("""
            Store Menu
            ----------
        1.  List all products in store
        2.  Show total amount in store
        3.  Make an order
        4.  Quit
        """))

        try:
            user_choice = int(input("Please choose a number: "))
            print()

            match user_choice:
                case 1: products_list(best_buy)
                case 2: products_quantity(best_buy)
                case 3: shopping_cart(best_buy)
                case 4: break

        except ValueError:
            print("Enter a number (see menu)")


def main():
    """Creates product list"""
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                ]

    best_buy = store.Store(product_list)

    start(best_buy)


if __name__ == "__main__":
    main()