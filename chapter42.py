def process_order(item, quantity):
    try:
        price = {"masala chai": 20 , "ginger tea": 15, "lemon tea": 10}
        cost = price[item] * quantity
        print(f"The total cost for {quantity} {item}(s) is: {cost}")
    except KeyError:
        print(f"Sorry, we do not have {item} available.")
    except TypeError:
        print("Invalid input. Please enter a valid item and quantity.") 
        
        
process_order("masala chai", 3)  # Valid input
process_order("green tea", 2)   # Invalid item
