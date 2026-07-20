def chai_customer():
    
    print("Welcome to the Chai Customer Service!")
    order = yield
    while True:
        print(f"Processing your order: {order}")
        order = yield
        
stall = chai_customer()
next(stall)  # Start the generator

stall.send("1 cup of chai")  # Send an order
stall.send("Ginger chai with extra sugar")  # Send another order
