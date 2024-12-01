#Area of Triangle
def area_triangle(base, height):
    base = float(base)
    height = float(height)

    result = ((1 / 2) * base * height)
    return result

#Perimeter of Triangle
def perimeter_triangle(s1, s2, s3):
    s1 = float(s1)
    s2 = float(s2)
    s3 = float(s3)

    result = s1 + s2 + s3
    return result

#Area of Circle
def area_circle(radius):
    radius = float(radius)

    result = ((22 / 7) * (radius ** 2))
    return result

#Circumference of Circle
def circumference_circle(radius):
    radius = float(radius)

    result = (2 * (22 / 7) * radius)
    return result

#Area of Square
def area_square(side):
    side = float(side)

    result = (side ** 2)
    return result

#Perimeter of Square
def perimeter_square(side):
    side = float(side)

    result = 4 * side
    return result

#Area of Rectangle
def area_rectangle(length, breadth):
    length = float(length)
    breadth = float(breadth)

    result = length * breadth
    return result

#Perimeter of Rectangle
def perimeter_rectangle(length, breadth):
    length = float(length)
    breadth = float(breadth)

    result = 2 * (length + breadth)
    return result