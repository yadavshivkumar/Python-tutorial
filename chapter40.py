from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied: Admins only.")
        else:
            return func(user_role)
    return wrapper  



@require_admin
def view_admin_dashboard(user_role):
    print("Welcome to the admin dashboard!")    
    
    