# decorators are functions that modify the behavior of other functions or methods. They are often used to add functionality to existing code without modifying the original function's code.

from functools import wraps


def my_decorator(func):
    @wraps(func)  # This preserves the original function's metadata
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator
def greet():
    print("Hello! from decorators class from chaicode ")
    print(greet.__name__)  # Output: greet  
    
    