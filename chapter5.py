essential_spice = ["cumin", "turmeric", "coriander", "paprika", "black pepper"] 
optional_spice = ["cinnamon", "nutmeg", "cloves", "cardamom", "saffron"]    

all_spices = essential_spice + optional_spice
print(f"All spices: {all_spices}")

common_spices = essential_spice & optional_spice
print(f"Common spices: {common_spices}")

only_in_essential = essential_spice - optional_spice
print(f"Spices only in essential: {only_in_essential}") 

print(f" Is 'cloves' in essential spices? {'cloves' in essential_spice} ")

unique_spices = set(all_spices)
print(f"Unique spices: {unique_spices}")    

frozenset_spices = frozenset(all_spices)
print(f"Frozenset of spices: {frozenset_spices}")   
print(f"Is 'saffron' in frozenset? {'saffron' in frozenset_spices}")    
