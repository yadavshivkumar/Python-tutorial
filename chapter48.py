class Chai:
    origin = "India"    
    
print(Chai.origin)

Chai.is_hot = True
print(Chai.is_hot)

masala = Chai()

print(f"Masala chai is from {masala.origin}")
print(f"Is the masala chai hot? {masala.is_hot}")

masala.is_hot = False
print(f"Is the masala chai hot? {masala.is_hot}")

