class Store:

    def __init__(self, product_list):
        self.product_list = product_list

    def add_product(self, product):
        """Adds a product to store."""
        self.product_list.append(product)

    def remove_product(self, product):
        """Removes a product from store."""
        self.product_list.remove(product)

    def get_total_quantity(self) -> int:
        """Returns how many items are in the store in total."""
        return sum(product.get_quantity() for product in self.product_list)

    def get_all_products(self): #-> list[Product]:
        """Returns all products in the store that are active."""
        return [product for product in self.product_list if product.is_active()]

    def order(self, shopping_list) -> float:
        """Calculates the total price of order."""
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price