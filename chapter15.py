menu = ["green salad", "chicken soup", "beef stew", "vegetable stir fry", "pasta primavera"]

for m in menu :
    print(f"Menu item is {m}")
    
for idx, item in enumerate(menu, start =1):
    print(f"{idx} : {item } chai")
    
while True:
    choice = input("Enter a menu item (or 'exit' to quit): ")
    if choice.lower() == 'exit':
        break
    elif choice in menu:
        print(f"You selected: {choice}")
    else:
        print("Item not found in the menu. Please try again.")  
    