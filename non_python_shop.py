class Chai:
    
    def __init__(self, sweetness, milk_level):
        self.swetness = sweetness
        self.milk_level = milk_level
        
    def sip(self):
         print("sipping chai")
         
    def add_sugar(self, amount):
        print("added the sugar")

my_chai = Chai(sweeetness= 3 , milk_level=2 )

my_chai.add_sugar(2)

