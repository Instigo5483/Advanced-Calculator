import sympy as sp

#Pythagoras Theorem
def pythagoras_theorem(base, height, hypotenuse):
    base = float(base)
    height = float(height)
    hypotenuse = float(hypotenuse)

    if (base == 0 and height > 0 and hypotenuse > 0):
        result = (((hypotenuse ** 2) - (height ** 2)) ** (1 / 2))
        return result
        
    elif (base > 0 and height == 0 and hypotenuse > 0):
        result = (((hypotenuse ** 2) - (base ** 2)) ** (1 / 2))
        return result

    elif (base > 0 and height > 0 and hypotenuse == 0):
        result = (((base ** 2) + (height ** 2)) ** (1 / 2))
        return result
    
    else:
        error = "Put '0' only to the value you want to find."
        return error
    
#Differentiation
def derivative(function, variable, order=1):
    x = sp.symbols(variable)
    func = sp.sympify(function)
    return sp.diff(func, x, order)

#Integration
def integration(function, variable, lower_limit=None, upper_limit=None):
    x = sp.symbols(variable)
    func = sp.sympify(function)
    
    if lower_limit is not None and upper_limit is not None:
        return sp.integrate(func, (x, lower_limit, upper_limit))
    else:
        return sp.integrate(func, x)
