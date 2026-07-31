class ChaiUtils:
    
    @staticmethod
    def clan_ingredients(text):
        # split by comma, strip whitespace and ignore empty items
        return [item.strip() for item in text.split(",") if item.strip() != ""]
       


raw = "water , milk , ginger , honey"

cleaned = ChaiUtils.clan_ingredients(raw)
print(cleaned)  # Output: ['water', 'milk', 'ginger', 'honey'] 
