class ChaiOrder:
    def __init__(self, type, size):
        self.type = type
        self.size = size

    def summary(self):
        return f"Chai Order: Type - {self.type}, Size - {self.size}"
    
    
order = ChaiOrder("Masala", "Large")
print(order.summary())


order_two = ChaiOrder("Green", "Medium")
print(order_two.summary())

        