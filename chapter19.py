staff = [("amit", 16), ("sachin", 18), ("rahul", 20), ("rohit", 22), ("virat", 24)  ]

for name, age in staff:
    if age >= 18:
        print(f"{name} is eligible for the job.")
        break
else:
    print("No eligible candidates found.")  
    
for name, age in staff:
    if age < 18:
        print(f"{name} is not eligible for the job.")
        break   
else:
    print("All candidates are eligible for the job.")   
    
    
for name, age in staff:
    if age >= 18:
        print(f"{name} is eligible for the job.")
    else:
        print(f"{name} is not eligible for the job.")   
        
print("All candidates have been evaluated.")
