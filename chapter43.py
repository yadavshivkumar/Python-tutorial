def brew_chai(flavour):
    if flavour not in ["masala", "ginger", "cardamom"]:
        raise ValueError("Invalid flavour. Choose from 'masala', 'ginger', or 'cardamom'.")
    print(f"Brewing {flavour} chai...") 
    

def serve_chai(flavour):
    print(f"Serving {flavour} chai. Enjoy your drink!") 
    
    if __name__ == "__main__":
        flavour = input("Enter the flavour of chai you want (masala, ginger, cardamom): ")
        brew_chai(flavour)
        serve_chai(flavour)     
        
    else:
        print("This module is intended to be run as a standalone script.")  
        
    