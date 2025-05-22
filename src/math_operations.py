def add(a,b):
    return a+b

def sub(a,b):
    return a-b 

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a/b

def power(base, exponent):
    """
    Calculate base raised to the power of exponent.
    
    Args:
        base: The base number
        exponent: The exponent to raise the base to
        
    Returns:
        The result of base^exponent
    
    Raises:
        ValueError: If trying to compute 0^0, which is mathematically undefined
    """
    if base == 0 and exponent == 0:
        raise ValueError("0^0 is undefined")
    return base ** exponent