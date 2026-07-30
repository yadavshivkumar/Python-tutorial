class chai:
    def __init__(self, type_, strength):
        self.type_ = type_
        self.strength = strength    
        
        
        
class GingerChai(chai):
    def __init__(self, type_, strength, ginger_amount):
        self.type_ = type_
        self.strength = strength
        self.ginger_amount = ginger_amount
        
class GingerChai(chai):
    def __init__(self, type_, strength, ginger_amount):
        chai.__init__(self, type_, strength)
        self.ginger_amount = ginger_amount
        
        
        
class GingeeChai(chai):
    def __init__(self, type_, strength, ginger_amount):
        super().__init__(type_, strength)
        self.ginger_amount = ginger_amount
        