#!/usr/bin/env python3
class Shoe:
    def __init__(self, brand, size):
        if not isinstance(size, int):
            raise ValueError("size must be an integer\n")
        self.brand = brand
        self.size = size
        self.color = None
        self.price = None

    def set_color(self, color):
        self.color = color

    def set_price(self, price):
        self.price = price

# Example usage:
try:
    nike_shoe = Shoe("Nike", "10")
except ValueError as e:
    print(e)
