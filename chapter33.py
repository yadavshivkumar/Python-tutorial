tea_prices_inr ={
    "Masala Chai": 50,
    "Green Tea": 40,    
    "Ginger Tea": 45,
}


tea_prices_usd = {tea: price / 75 for tea, price in tea_prices_inr.items()}
print(tea_prices_usd)

if __name__ == "__main__":
    print("Tea prices in USD:")
    for tea, price in tea_prices_usd.items():
        print(f"{tea}: ${price:.2f}")   
        
    while True:
        tea_choice = input("Enter the tea you want to buy (or type 'exit' to quit): ")
        if tea_choice.lower() == 'exit':
            break
        elif tea_choice in tea_prices_usd:
            print(f"The price of {tea_choice} is ${tea_prices_usd[tea_choice]:.2f}")
        else:
            print("Sorry, we don't have that tea. Please choose from the available options.")       
            
else:
    print("This module is being imported, not run directly.")   
    
    
print("Available teas:")
