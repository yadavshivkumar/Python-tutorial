from functools import wraps


def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished function: {func.__name__}")
        return result
    return wrapper


@log_activity
def brew_chai(type):
    print(f"Brewing {type} chai...")
    return f"{type} chai is ready!" 

if __name__ == "__main__":
    print(brew_chai("Masala"))  
    
else:
    print("This module is being imported, not run directly.")
    
    
print("This is a test message to demonstrate the decorator functionality.")