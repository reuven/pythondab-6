#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''    
    sc = ShoppingCart()
    sc.add('book', 30, 1)    # name, price-per-unit, quantity
    sc.add('toothbrush', 3, 4)

    sc.remove('toothbrush')   # removes one toothbrush -- or removes
                              # the item altogether if the quantity is 0
    
    sc.total()  # returns the total price of items in the shopping cart
'''

class ShoppingCart(object):
  def __init__(self):
    self.items = []

  def add(self, item_name, price_per_unit, quantity):
    item = (item_name, price_per_unit, quantity)
    self.items.append(item)

  def remove(self, name):
    for item in self.items:
      if item[0] == name:
        self.items.remove(item)
        break

  def total(self):
    total = 0
    for item in self.items:
      total += item[1]*item[2]
    return total
  
def main():
  sc = ShoppingCart()
  items = [("apple", 2, 10), ("orange", 1, 7), ("banana", 1, 3), ("papaya", 4, 9)]
  for item in items:
    sc.add(item[0], item[1], item[2])

  print("\nShopping Cart Items:")
  for item in sc.items:
      print(f"A {item[0]} costs ${item[1]} and there are {item[2]} in your cart.")

  total = sc.total()
  print(f"\nThe total for this shopping cart: ${total}\n")

  sc.remove(item[0])

  print("\nShopping Cart Items:")
  for item in sc.items:
      print(f"A {item[0]} costs ${item[1]} and there are {item[2]} in your cart.")

  total = sc.total()
  print(f"\nThe total for this shopping cart: ${total}\n")

if __name__ == "__main__":
    main()