#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Recipe:
  def __init__(self, title, description, ingredients =[]):
    self.title = title
    self.description = description
    self.ingredients = ingredients

  def __repr__(self):
    output = f"Title: {self.title}\nDescription: {self.description}\nIngredients: {self.ingredients}\n"
    return output

class Ingredient:
  def __init__(self, name, quantity, units):
    self.name = name
    self.quantity = quantity
    self.units = units

  def __repr__(self):
    output = f"{self.quantity} {self.units} of {self.name}"
    return output

def main():
  ing1 = Ingredient('apple', 2, 'each')
  ing2 = Ingredient('salt', 2, 'pinch')
  ing3 = Ingredient('sugar', 1, 'pinch')
  recipe1 = Recipe('Apple Pie', 'A delicious apple pie', [ing1, ing2, ing3])
  recipe2 = Recipe('Pie, without ingredients', 'An abstract pie') # without specifying ingredients
  
  print(recipe1)
  print(recipe2)

if __name__ == "__main__":
    main()