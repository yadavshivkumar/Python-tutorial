class Chaicup:
    size = 150  # in ml
    
    def describe(self):
        return f"A {self.size} ml cup of chai."
    
cup = Chaicup()
print(cup.describe())   
print(Chaicup.describe())


cup_two = Chaicup()
cup_two.size = 200
print(Chaicup.describe(cup_two))  # This will raise an error because describe() is an instance method and expects an instance as the first argument.    


