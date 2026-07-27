class Chai:
    temperature = "hot"
    strength = "Strong"
    
    
cutting = Chai()
print(cutting.temperature)

cutting.temperature = "mild"

print("After changing", cutting.temperature)
print("cup size is ", cutting.size)
print("Direct look into the class ", Chai.temperature)

del cutting.temperature
print(cutting.temperature)

