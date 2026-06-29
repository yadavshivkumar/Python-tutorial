# List are mutable, ordered sequences of elements.
# They can contain elements of different data types, including other lists.
# Lists are defined by enclosing elements in square brackets [] and separating them with commas. 


# Example of a list:
my_list = [1, 2, 3, 'four', 'five', [6, 7, 8]]  

ingredients = ['flour', 'sugar', 'eggs', 'milk', 'butter']
ingredients.append('vanilla')  # Adding an element to the end of the list
print(f"Ingredients are: {ingredients}")

ingredients.remove('sugar')  # Removing an element from the list
print(f"Ingredients are: {ingredients}")

ingredients.insert(2, 'baking powder')  # Inserting an element at a specific index
print(f"Ingredients are: {ingredients}")   

ingredients.sort()  # Sorting the list in ascending order
print(f"Ingredients are: {ingredients}")

spice_options = ['cinnamon', 'nutmeg', 'cloves', 'ginger']
# Combining two lists using the extend() method
ingredients.extend(spice_options)
print(f"Ingredients are: {ingredients}")

#pop is used to remove an element at a specific index and return it. If no index is specified, it removes and returns the last item in the list.
last_ingredient = ingredients.pop()  # Removes the last item
print(f"Removed ingredient: {last_ingredient}") 
ingredients.pop(2)  # Removes the item at index 2
print(f"Ingredients are: {ingredients}")    

#reverse() method reverses the order of the list in place.
ingredients.reverse()  # Reversing the order of the list
print(f"Ingredients are: {ingredients}")    

#sort() method sorts the list in ascending order. If you want to sort in descending order, you can use the reverse parameter.
#append() method adds an element to the end of the list.
#remove() method removes the first occurrence of a specified value from the list.
#insert() method inserts an element at a specified index in the list.
#pop() method removes an element at a specific index and returns it.    
#index() method returns the index of the first occurrence of a specified value in the list. 
#max() method returns the largest item in the list.
#min() method returns the smallest item in the list.


base_liquid = ['water', 'milk', 'juice', 'soda']
extra_flavor =["ginger"]

full_liquid_mix = base_liquid + extra_flavor  # Combining two lists using the + operator
print(f"Full liquid mix: {full_liquid_mix}")

strong_brew = ["black tea" , "water"] * 3  # Repeating a list multiple times
print(f"Strong brew: {strong_brew}")

raw_spice_data  = bytearray(b"CINNAMON")
print(f"Raw spice data: {raw_spice_data}")

