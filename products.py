class Product:

    def __init__(self, name, price, quantity):

        # validate name
        if not name.strip():
            raise ValueError("name must be a non-empty string")
        # validate price
        try:
            price = float(price)
        except Exception:
            raise ValueError("price must be a number")
        if price < 0:
            raise ValueError("price must be >= 0")
        # validate quantity
        try:
            quantity = int(quantity)
        except Exception:
            raise ValueError("quantity must be an integer")
        if quantity < 0:
            raise ValueError("quantity must be >= 0")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity):
        """Updates quantity and product's status (active or not)"""
        try:
            quantity = int(quantity)
        except Exception:
            raise ValueError("quantity must be an integer")
        if quantity < 0:
            raise ValueError("quantity must be >= 0")

        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()
        else:
            self.activate()

    def is_active(self) -> bool:
        """Returns True if product is active (in stock), otherwise False."""
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        """Displays product information."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.get_quantity()}")

    def buy(self, quantity) -> float:
        """Handles purchase logic and returns total price."""
        try:
            quantity = int(quantity)
        except Exception:
            raise ValueError("quantity must be an integer")
        if quantity <= 0:
            raise ValueError("quantity to buy must be >= 1")

        if not self.active:
            return f"Cannot buy '{self.name}' — product is inactive or out of stock."
        if quantity > self.quantity:
            return f"Not enough stock of '{self.name}'. Only {self.quantity} left."

        self.set_quantity(self.quantity - quantity)

        total_price = self.price * quantity

        return f"You bought {quantity} of {self.name} for a total of {total_price}"

bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

# print(bose.buy(50))
# print(mac.buy(100))
# print(mac.is_active())

# bose.show()
# mac.show()

# bose.set_quantity(1000)
# bose.show()

# mac.set_quantity(1000)
# mac.show()
# print(mac.is_active())