from abc import ABC, abstractmethod

# Product class
class Product:
    def __init__(self, product_id, name, price, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} - ₹{self.price}"

# Cart class
class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity=1):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def remove_product(self, product):
        if product in self.items:
            del self.items[product]

    def view_cart(self):
        print("\n🛒 Cart Items")
        if not self.items:
            print("Your cart is empty.")
            return 0
        total = 0
        for product, quantity in self.items.items():
            print(f"{product.name} * {quantity} = ₹{product.price * quantity}")
            total += product.price * quantity
        print("Total amount =", total)
        return total

# Abstract class for payment
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Polymorphism: Credit Card
class CreditCardMethod(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} via Credit Card")

# Polymorphism: UPI
class UPI(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} via UPI")

# User class
class User:
    def __init__(self, username):
        self.username = username
        self.cart = Cart()

# Order class
class Order:
    def __init__(self, user, payment_method):
        self.user = user
        self.payment_method = payment_method

    def checkout(self):
        total = self.user.cart.view_cart()
        if total == 0:
            print("Cart is empty. Add items before checkout.")
        else:
            self.payment_method.pay(total)
            print(f"Thank you, {self.user.username}, for your order!")

# ----------- Main Program -----------

# Product catalog
catalog = [
    Product(1, "Laptop", 60000, "Electronics"),
    Product(2, "Headphones", 2000, "Electronics"),
    Product(3, "Book", 400, "Books"),
    Product(4, "T-shirt", 500, "Fashion")
]

# Set of unique categories
unique_categories = set(p.category for p in catalog)

# Display available products
def display_catalog():
    print("\nAvailable Products:")
    for p in catalog:
        print(f"{p.product_id}. {p}")

# Menu-driven interaction
def main():
    print("👋 Welcome to the Online Shopping Cart!")
    username = input("Enter your name: ")
    user = User(username)

    while True:
        print("\n--- Menu ---")
        print("1. View Product Catalog")
        print("2. Add Product to Cart")
        print("3. Remove Product from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Enter your choice (1–6): ")

        if choice == "1":
            display_catalog()

        elif choice == "2":
            display_catalog()
            pid = int(input("Enter product ID to add: "))
            quantity = int(input("Enter quantity: "))
            product = next((p for p in catalog if p.product_id == pid), None)
            if product:
                user.cart.add_product(product, quantity)
                print("✅ Product added to cart.")
            else:
                print("❌ Invalid product ID.")

        elif choice == "3":
            if not user.cart.items:
                print("Your cart is empty.")
                continue
            user.cart.view_cart()
            pid = int(input("Enter product ID to remove: "))
            product = next((p for p in catalog if p.product_id == pid), None)
            if product and product in user.cart.items:
                user.cart.remove_product(product)
                print("✅ Product removed from cart.")
            else:
                print("❌ Product not in cart.")

        elif choice == "4":
            user.cart.view_cart()

        elif choice == "5":
            print("Choose Payment Method:")
            print("1. UPI")
            print("2. Credit Card")
            pay_choice = input("Enter choice (1 or 2): ")
            if pay_choice == "1":
                payment = UPI()
            elif pay_choice == "2":
                payment = CreditCardMethod()
            else:
                print("❌ Invalid payment method.")
                continue
            order = Order(user, payment)
            order.checkout()

        elif choice == "6":
            print("🛑 Exiting... Thank you for visiting!")
            break

        else:
            print("❌ Invalid choice. Please try again.")

# Run the program
main()
