def update_order():
    chai_type = "Elachi Chai"
    
    def kitchen():
        nonlocal chai_type
        chai_type = "Masala Chai"
    kitchen()
    print("After kitchen update", chai_type)
    
update_order()

 