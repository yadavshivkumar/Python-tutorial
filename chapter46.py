file = open("menu.txt", "r")

try:
    file.read()
except Exception as e:
    print("Error:", e)
finally:
    file.close()
    
with open("menu.txt", "r") as file:
    try:
        file.read()
    except Exception as e:
        print("Error:", e)
        
