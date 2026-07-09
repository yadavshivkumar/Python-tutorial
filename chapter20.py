#walrus operator
# The walrus operator (:=) allows you to assign values to variables as part of an expression. 
# This can make your code more concise and readable by reducing the need for separate assignment statements.    


value = 13
remainder = value % 2

if remainder:
    print(f"Not divisible, remainder is {remainder} ")
    

value = 13

if (remainder := value % 2):
    print(f"Not divisible, remainder is {remainder} ")
    

else:
    print("Divisible by 2") 
    
    
 
    
    

available_sizes = ["small", "medium", "large"]

if(requested_size := input("Enter your chai cup size: ")) in available_sizes:
    print(f"serving {requested_size} chai ")
    
else:
    print(f"Sorry, we don't have {requested_size} size available. Please choose from {available_sizes}.")   
    






flavors = ["vanilla", "chocolate", "strawberry", "mint", "coffee"]
print("Available flavors: ", flavors)

if (requested_flavor := input("Enter your flavor: ")) in flavors:
    print(f"Serving {requested_flavor} flavor.")
    
else:
    print(f"Sorry, we don't have {requested_flavor} flavor available. Please choose from {flavors}.")           
    
  