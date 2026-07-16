#pure functions are functions that always return the same output for the same input and have no side effects. 
# They do not modify any external state or variables, and they do not depend on any external state or variables.    


# impure fuctions are functions that may have side effects or depend on external state or variables.    

#recursive functions are functions that call themselves in order to solve a problem. They typically have a base case that stops the recursion and a recursive case that breaks the problem down into smaller subproblems.   

# lambada functions are anonymous functions that can take any number of 
# arguments but can only have one expression. They are often used as a shorthand for defining small, simple functions.    


chai_type = {"Elachi Chai": "Masala Chai", "Adrak Chai": "Ginger Chai", "Tulsi Chai": "Holy Basil Chai", "Kesar Chai": "Saffron Chai", "Elaichi Adrak Chai": "Cardamom Ginger Chai" }

strong_chai = list(filter(lambda x: "Chai" in x, chai_type.keys()))
print(strong_chai)  

if "Adrak Chai" in chai_type:   
    print("Adrak Chai is available in the menu.")


else:
    print("Adrak Chai is not available in the menu.")   
    
if "Tulsi Chai" in chai_type:   
    print("Tulsi Chai is available in the menu.")
else:       
    print("Tulsi Chai is not available in the menu.")
    
    
if "Kesar Chai" in chai_type:   
    print("Kesar Chai is available in the menu.")
else:
    print("Kesar Chai is not available in the menu.")
    
    
if "Elaichi Adrak Chai" in chai_type:   
    print("Elaichi Adrak Chai is available in the menu.")
    
else:
    print("Elaichi Adrak Chai is not available in the menu.")