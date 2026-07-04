for token in range(1,11):
    print(f"Serving chai to Token #{token}")
    
tokens = ["Token1", "Token2", "Token3", "Token4", "Token5"]
for token in tokens:
    print(f"Serving chai to {token}")   
    
tokens = ["Token1", "Token2", "Token3", "Token4", "Token5"]
while tokens:
    token = tokens.pop(0)  # Remove the first token from the list
    print(f"Serving chai to {token}")  # Serve chai to the token    
    
while True:
    token = input("Enter token number to serve chai (or type 'exit' to stop): ")
    if token.lower() == 'exit':
        break  # Exit the loop if the user types 'exit'
    print(f"Serving chai to Token #{token}")  # Serve chai to the entered token number  
    
    
    
