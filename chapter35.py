# generators are a simple and powerful tool for creating iterators. 
# They are written like regular functions but use the yield statement whenever they want to return data. Each time next() is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed).


def serve_chai ():
    print("Serving Chai")
    yield "Chai"
    print("Serving another Chai")
    yield "Chai"
    print("Serving yet another Chai")
    yield "Chai"    
    
stall = serve_chai()  # This will not print anything yet, as the generator has not been executed.

for cup in stall:
    print(f"Enjoy your {cup}!")  # This will print "Enjoy your Chai!" three times, with the corresponding serving messages in between.  
    
def get_chai_list():
    return ["cup 1", "cup 2", "cup 3"   ]
def get_chai_generator():
    yield "cup 1"
    yield "cup 2"
    yield "cup 3"   
    
chai = get_chai_generator()  # This will create a generator of chai cups.
print(next(chai))  # This will print "cup 1"
print(next(chai))  # This will print "cup 2"
print(next(chai))  # This will print "cup 3"

0