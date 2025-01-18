#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Item:
  def __init__(self, name, price, quantity):
    self.name = name
    self.unitPrice = price
    self.quantity = quantity
  
  def show(self):
    print(f"{self.name}: ${self.unitPrice} ({self.quantity} available)")

class ShoppingCart(object):
  
  def __init__(self):
    # a list of items
    self.itemList = []
    self.quantity = []

  def add(self, name):
    """ """
    self.itemList.append(name)

  def remove(self, name):
    """  """
    idx = self.itemList.index(name)
    self.itemList.remove(name)

  def total(self):
    """ print the subtotals of all items  """
    total = 0
    #subtotalList = ShoppingCart.subtotal(self)
    print ("Name\tPrice\tQuantity Subtotal")
    for idx in range(len(self.itemList)):
      name = self.itemList[idx].name
      unitPrice = self.itemList[idx].unitPrice
      quantity = self.itemList[idx].quantity
      print(f"{name} \t {quantity} \t {unitPrice} \t {unitPrice*quantity}")
    #print("Total Cost of the Shopping Cart is {}".format(total))

def main():
  sc = ShoppingCart()
  items = [Item("apple", 2, 10), Item("orange", 1, 10), Item("banana", 3, 10), Item("papaya", 7, 10)]
  for item in items:
    sc.add(item)
  sc.total()
  sc.remove(items[0])
  sc.total()
  sc.remove(items[1])
  sc.total()
  sc.remove(items[2])
  sc.total()

if __name__ == "__main__":
    main()