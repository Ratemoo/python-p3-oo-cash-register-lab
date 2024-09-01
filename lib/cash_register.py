#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        """Initialize the CashRegister with an optional discount."""
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = (None, 0)  # To track the last transaction

    def add_item(self, title, price, quantity=1):
        """Add items to the register, update the total and store last transaction details."""
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.last_transaction = (title, price * quantity)

    def apply_discount(self):
        """Apply the discount to the total price and print the result."""
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """Subtract the last transaction amount from the total."""
        if self.last_transaction[0] is not None:
            title, amount = self.last_transaction
            self.total -= amount
            # Remove the last transaction items from the items list
            if self.items:
                # Find the number of items and remove them
                count = self.items.count(title)
                if count > 0:
                    self.items = [item for item in self.items if item != title]
                    self.last_transaction = (None, 0)  # Reset the last transaction

    def count_sentences(self):
        """Count the number of sentences in the total amount string."""
        import re
        
        # Convert total to string and split by sentence-ending punctuation
        total_string = f"{self.total}"
        sentences = re.split(r'[.!?]', total_string)
        sentences = [s.strip() for s in sentences if s.strip()]
        return len(sentences)
