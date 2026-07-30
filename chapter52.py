class Basechai:
    def __init__(self, type_):
        self.type_ = type_
        
    def prepare(self):
        print(f"Preparing {self.type_} basechai.")
        


class MasalaChai(Basechai):
    def add_spices(self):
        print("Adding Cardamom to the masala chai.")
        
class GingerChai(Basechai):
    def add_ginger(self):
        print("Adding Ginger to the ginger chai.")
        

