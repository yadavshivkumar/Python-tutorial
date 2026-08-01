class ChaiOrder:
    
    def __init__(self, tea_type, size, sugar_level):
        self.tea_type = tea_type
        self.size = size
        self.sugar_level = sugar_level
        
    
@classmethod 
def from_dict(cls, order_data):
    return cls(
        order_data['tea_type'],
        order_data['size'],
        order_data['sugar_level']
    )


@classmethod
def from_string(cls, order_string):
    tea_type, size, sugar_level = order_string.split('-')
    return cls(tea_type.strip(), size.strip(), sugar_level.strip()) 
        
        

order1 = ChaiOrder.from_dict({'tea_type': 'Masala Chai', 'size': 'Large', 'sugar_level': 'Medium'})
order2 = ChaiOrder.from_string('Green Tea - Small - Low')


        
        