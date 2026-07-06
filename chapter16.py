name = ["Alice", "Bob", "Charlie" , "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"   ]

bill = [120, 150, 200, 80, 90, 110, 130, 170, 160, 140] 

for name, amount in zip(name, bill):
    print(f"Name: {name} paid Bill: ${amount}")

while True:
    choice = input("Enter a name to check their bill (or 'exit' to quit): ")
    if choice.lower() == 'exit':
        break
    elif choice in name:
        index = name.index(choice)
        print(f"{choice} paid Bill: ${bill[index]}")
    else:
        print("Name not found. Please try again.")  
        
        