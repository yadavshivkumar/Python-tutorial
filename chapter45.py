class InvalidChaiError(Exception):
    pass
    
def bill(flavour, cups):
    menu = {
        "masala": 20,
        "ginger": 25,   
        "cardamom": 30,
        "plain": 15
    }
    try:
        if flavour not in menu:
            raise InvalidChaiError(f"Invalid chai flavour: {flavour}")
        if not isinstance(cups, int) :
            raise TypeError("Number of cups must be a positive integer.")
        total = menu[flavour] * cups
        print(f"Total bill for {cups} cups of {flavour} chai is: Rs. {total} ")
     
    except Exception as e:
        print("Error:", e)
        
    finally:
        print("Thank you for visiting our chai shop!")
        
        
bill("masala", 3)   
bill("ginger", 2)
bill("cardamom", 4)
bill("plain", 5)