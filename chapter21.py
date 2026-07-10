users =  [
    {"id": 1 , "total": 100, "coupon": "P20"},
    {"id": 2 , "total": 200, "coupon": "s20"},
    {"id": 3 , "total": 300, "coupon": "N20"},

]

discount = {
    "P20": (0.2, 0),
    "s20": (0.1, 0),
    "N20": (0, 20)
}

for user in users:
    percent, fixed = discount.get(user["coupon"], (0, 0))
    discount_amount = user["total"] * percent + fixed
    final_total = user["total"] - discount_amount
    print(f"User ID: {user['id']}, Original Total: {user['total']}, Discount Amount: {discount_amount}, Final Total: {final_total}")    
    
        