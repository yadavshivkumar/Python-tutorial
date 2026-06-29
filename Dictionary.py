# Dictionary is a data structure that stores key-value pairs.
# It allows for efficient retrieval, insertion, and deletion of 
# values based on their associated keys. 
# 
# In Python, dictionaries are implemented as hash tables, 
# which provide average-case constant time complexity for these operations.

# it is a mutable data structure, meaning that the contents of a dictionary
# can be changed after it is created.     

chai_order = dict(type='chai', size='medium', sugar='2 tsp', milk='whole')

print(f"Chai Order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "water"

print(f"Chai Recipe: {chai_recipe['base']} with {chai_recipe['liquid']} ")

del chai_recipe["liquid"]
print(f"Chai Recipe after deletion: {chai_recipe}") 

print(f"Is sugar in the order? {'sugar' in chai_order}  ")

chai_order = {"type": "chai", "size": "medium", "sugar": "2 tsp", "milk": "whole"   }

print(f"Order details (keys): {list(chai_order.keys())} ")
print(f"Order details (values): {list(chai_order.values())} ")


last_item = chai_order.popitem()
print(f"Last item removed from order: {last_item} ")

extra_spices = {"cardamom": "1 tsp", "cinnamon": "1/2 tsp"} 
chai_order.update(extra_spices) 
print(f"Updated Chai Order with extra spices: {chai_order} ")

