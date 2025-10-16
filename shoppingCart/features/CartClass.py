#!/usr/bin/python3
# CartClass.py

class ShoppingCart:
    def __init__(self):
        self.items = {}  # {title: {'price': price, 'quantity': quantity}}

    def add_book(self, title, price):
        """Adds a book or increases quantity if it exists."""
        price = float(price)
        if title in self.items:
            self.items[title]['quantity'] += 1
        else:
            self.items[title] = {'price': price, 'quantity': 1}

    def remove_book(self, title):
        """Removes a book item completely from the cart."""
        if title in self.items:
            del self.items[title]

    def empty_cart(self):
        """Removes all items from the cart."""
        self.items = {}

    @property
    def total_items(self):
        """Returns the number of unique book titles in the cart."""
        return len(self.items)

    @property
    def total_books(self):
        """Returns the sum of quantities of all books."""
        return sum(item['quantity'] for item in self.items.values())

    @property
    def total_sum(self):
        """Calculates the total monetary sum of the cart."""
        total = sum(item['price'] * item['quantity'] for item in self.items.values())
        return round(total, 2)