def chai_flavour(flavour="masala"):
    """Return the flavour of the chai."""
    chai="ginger"
    return flavour


print(chai_flavour.__doc__)  
print(chai_flavour.__name__)  

def generate_bill(chai=0, samosa= 0):
    """calculate the total bill for chai and samosa.
    :param chai: number of chai cups
    :param samosa: number of samosas
    :return: total bill amount
    """
    
    total_bill = (chai * 10) + (samosa * 20)
    return total_bill

print(generate_bill(chai=2, samosa=3))  # Output: 80