flavours = ["gingers", "out of stock", "lemon", "Discontinued", "Tulsi"]

for flavour in flavours:
    if flavour == "out of stock":
        continue
    if flavour == "Discontinued ":
        break
    print(f"{flavour} item found!")
    
    

print(f"Out of Stock flavours: {flavours.count('out of stock')}")


    
while True:
    flavour = input("Enter a flavour (or 'exit' to quit): ")
    if flavour == "exit":
        break
    if flavour == "out of stock":
        print("This flavour is currently out of stock.")
        continue
    if flavour == "Discontinued":
        print("This flavour has been discontinued.")
        break
    print(f"You selected: {flavour}")   
    