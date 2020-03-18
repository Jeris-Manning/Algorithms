#!/usr/bin/python

recipe = { 'milk': 2, 'sugar': 40, 'butter': 20 }
ingredients = { 'milk': 5, 'sugar': 120, 'butter': 500 }

import math

def recipe_batches(recipe, ingredients):

    if len(recipe)>len(ingredients):
        return 0
    max_batches = ingredients[list(ingredients.keys())[0]]
    for goods in recipe:
        if ingredients[goods] // recipe[goods] < max_batches:
            max_batches = ingredients[goods] // recipe[goods]
    return max_batches




if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))