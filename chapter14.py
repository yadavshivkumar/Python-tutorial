orders = [ "shivam", "rahul", "sita", "gita", "ram" ]

for name in orders :
    print(f"Order ready for{name}")
    
while True: 
    name = input("Enter your name to collect the order: ")
    if name in orders:
        print(f"Order collected by {name}")
        orders.remove(name)
    else:
        print("No order found for your name.")
    
    if not orders:
        print("All orders have been collected.")
        break
    