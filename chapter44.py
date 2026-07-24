class OUTofIngredientsError(Exception):
    pass

def make_chai(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OUTofIngredientsError("Not enough ingredients to make chai.")
    print("Chai is ready!   Enjoy your drink!")
    

def main():
    try:
        make_chai(0, 1)
    except OUTofIngredientsError as e:
        print(e)    
    
    if __name__ == "__main__":
        main()  
        print("Program continues after handling the exception.")
        
print("This is the end of the program.")

