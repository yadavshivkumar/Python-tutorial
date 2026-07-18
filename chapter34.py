daily_sales = [100, 150, 200, 180, 220, 300, 250, 400, 350, 500]

total_cups = sum(sale for sale in daily_sales if sale > 200)

print(total_cups)

if total_cups > 1000:
    print("Great job! You sold a lot of cups today!")
    
elif total_cups > 500:
    print("Good job! You sold a decent amount of cups today!")

elif total_cups > 300:
    print("Not bad! You sold some cups today!")
    
elif total_cups > 100:
    print("You sold a few cups today. Keep trying!")
    
else:
    print("Keep going! You can sell more cups tomorrow!")
    