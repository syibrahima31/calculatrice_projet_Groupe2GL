def add(x:float, y:float) -> float: 
    """
        arguments: 
            x : argument 
            y : argument 
        return: 
            result (float)
    """
    return x + y 

def sub(x:float, y:float) -> float: 
    """
        arguments: 
            x : argument 
            y : argument 
        return: 
            result (float)
    """
    return x - y 

def mult(x:float, y:float) -> float: 
    """
        arguments: 
            x : argument 
            y : argument 
        return: 
            result (float)
    """
    return x * y 

def div(x:float, y:float) -> float: 
    """
        arguments: 
            x : argument 
            y : argument  non nul 
        return: 
            result (float)
    """
    if y == 0: 
        raise ZeroDivisionError("On ne divise pas par zero")
    return x / y 
