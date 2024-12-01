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
        return print(error)