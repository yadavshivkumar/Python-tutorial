def serve_chai():
    chai_type= "Masala Chai"
    print(f"Inside Function {chai_type}")
    
    

chai_type = "Lemon Chai "
serve_chai()
print(f"Outside Function {chai_type}")

def chai_counter():
    chai_order = "Lemon Chai"
    
    def print_order():
        chai_order = "Lemon Chai"
        print("Inner:", chai_order)
    print_order()
    print("Outer:", chai_order)
    
    
chai_order = "Tulsi Chai"
chai_counter()  
print("Global:", chai_order)

