# error handling is important in programming to ensure that your code can
# gracefully handle unexpected situations and continue to run without crashing.
# In Python, error handling is typically done using try-except blocks. 
# Here's a basic example:    

# Exception handling in Python allows you to catch and handle errors that may
# occur during the execution of your code. This helps prevent your program from 
#  crashing and allows you to provide meaningful feedback to the user or take corrective actions.  

chai_menu = {"masala": 30, "ginger": 25, "cardamom": 35, "plain": 20}

try:
    chai_menu["Elaichi"]
    
except KeyError:
    print("The requested chai flavor is not available in the menu.")
    
print("Program continues to run smoothly after handling the error.")


if __name__ == "__main__":
    # You can add more code here to test other functionalities or handle different exceptions.
    pass    
    print("This is the main block of the program. You can add more functionality here.")    
    
    
else:
    print("This code is being imported as a module, not run directly.") 
    
    
    
print("End of the program.")    