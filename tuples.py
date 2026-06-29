# Tuples is a built-in data structure in Python that is used to store 
# multiple items in a single variable. Tuples are similar to lists, 
# but they are immutable, meaning that once a tuple is created, its 
# elements cannot be changed, added, or removed.
# Tuples are defined by enclosing the elements in parentheses `()`.  

masala_spices = ("cumin", "coriander", "turmeric", "chili powder", "garam masala")  

print(f"Main masala spices are: {masala_spices[0]}, {masala_spices[1]}, {masala_spices[2]}, {masala_spices[3]}, and {masala_spices[4]   }.   ")

ginger_ratio, cardamon_ration = 2,  1
print(f"Ginger to cardamon ratio is {ginger_ratio}:{cardamon_ration}")

# membership test

print("Cumin is present in the masala spices tuple.")   
    
print(f"Is ginger present in the masala spices tuple? {'ginger' in masala_spices}   ")
    
print(f"Is cardamon present in the masala spices tuple? {'cardamon' in masala_spices}   ")  

#membership is used to check if an element is present in a tuple or not. It returns True if the element is present, otherwise it returns False. 

#Tuples can also be used to return multiple values from a function. For example, a function can return a tuple containing multiple values, which can then be unpacked into separate variables.  

