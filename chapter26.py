def add_vat(price, vat_rate):
    return price + (price * vat_rate / 100)


orders = [100, 200, 300]


for price in orders:
   final_amount = add_vat(price, 10)
   
   print(f"Original Price: {price}, Final Amount with VAT: {final_amount}")
   
