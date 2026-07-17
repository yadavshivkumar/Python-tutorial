favourite_chai= [
    "Masala Chai", "Green Tea", "Ginger Tea", "Lemon Tea", 
    "Tulsi Tea", "Black Tea", "Oolong Tea", "Chamomile Tea", 
    "Peppermint Tea", "Hibiscus Tea"    
    
]

unique_chai ={chai for chai in favourite_chai }
print(unique_chai)

recipe = {
    "Masala Chai": "A spiced tea made with black tea, milk",
    "Green Tea": "A mild tea made with green tea leaves",
    "Ginger Tea": "A warming tea made with fresh ginger",
    "Lemon Tea": "A citrusy tea made with lemon juice",
    "Tulsi Tea": "An herbal tea made with holy basil",
    "Black Tea": "A robust tea made with black tea leaves",
    "Oolong Tea": "A semi-oxidized tea made with oolong tea leaves",
    "Chamomile Tea": "A calming tea made with chamomile flowers",
    "Peppermint Tea": "A refreshing tea made with peppermint leaves",
    "Hibiscus Tea": "A tart tea made with hibiscus flowers"
}

unique_spices = {spice for description in recipe.values() for spice in description.split(", ")  }

print(unique_spices)        
