import math
import Libraries.shapes_formula as shapes_formula

while True:
    print("""----------------------------------------------------------------
        1.  Addition -> (+)
        2.  Subtraction -> (-)
        3.  Multiplication -> (*)
        4.  Division -> (/)
        5.  Modulus -> (%)
        6.  Floor Division -> (//)
        7.  Exponential -> (**)
        8.  Permutation -> (perm)
        9.  Combination -> (comb)
        10. Logarithm -> (log)
        11. Radians to Degrees -> (rtd)
        12. Degrees to Radians -> (dtr)
        13. Shapes Calculations -> (sc)
        14. Exit -> (exit)
----------------------------------------------------------------""")
    
    operator = input("Choose an operation: ")

    if (operator.lower() == 'exit'):
        print("Exiting the program.")
        break

    elif (operator in ['+', '-', '*', '/', '%', '//', '**'] or operator.lower() in ['perm', 'comb', 'log', 'rtd', 'dtr']):
        try:
            #Addition
            if (operator == '+'):
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
    
                print(f"The addition is: {num1 + num2}")
                continue
            
            #Subtraction
            elif (operator == '-'):
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
    
                print(f"The subtraction is: {num1 - num2}")
                continue
            
            #Multiplication
            elif (operator == '*'):
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
    
                print(f"The multiplication is: {num1 * num2}")
                continue
    
            #Division
            elif (operator == '/'):
                num1 = float(input("Enter the dividend: "))
                num2 = float(input("Enter the divisor: "))
    
                if (num2 == 0):
                    print("Error: Division by zero is not allowed.")
    
                else:
                    print(f"The division is: {num1 / num2}")
                continue
    
            #Modulus
            elif (operator == '%'):
                num1 = float(input("Enter the dividend: "))
                num2 = float(input("Enter the divisor: "))
    
                if (num2 == 0):
                    print("Error: Modulus by zero is not allowed.")
    
                else:
                    print(f"The modulus is: {num1 % num2}")
                continue
    
            #Floor Division
            elif (operator == '//'):
                num1 = float(input("Enter the dividend: "))
                num2 = float(input("Enter the divisor: "))
    
                if (num2 == 0):
                    print("Error: Floor Division by zero is not allowed.")
    
                else:
                    print(f"The floor division is: {num1 // num2}")
                continue
    
            #Exponential
            elif (operator == '**'):
                num1 = float(input("Enter the number: "))
                num2 = float(input("Enter the power: "))
    
                print(f"The exponential is: {num1 ** num2}")
                continue
    
            #Permutation
            elif (operator == 'perm'):
                num1 = float(input("Enter the first number(n): "))
                num2 = float(input("Enter the second number(k): "))
    
                if (num1 < num2):
                    print("Error: 'n' must be greater than or equal to 'k'.")
    
                else:
                    print(f"The permutation is: {math.comb(num1, num2)}")
                continue
    
            #Combination
            elif (operator.lower() == 'comb'):
                num1 = float(input("Enter the first number(n): "))
                num2 = float(input("Enter the second number(k): "))
    
                if (num1 < num2):
                    print("Error: 'n' must be greater than or equal to 'k'.")
    
                else:
                    print(f"The combination is: {math.comb(num1, num2)}")
                continue
    
            #Logarithm
            elif (operator.lower() == 'log'):
                num1 = float(input("Enter the base number: "))
                num2 = float(input("Enter the logarithm base: "))
    
                if (num1 <= 0 or num2 <= 0):
                    print("Error: Base and logarithm base must be positive.")
    
                else:
                    print(f"The logarithm is: {math.log(num1, num2)}")
                continue
    
            #Radians to Degrees
            elif (operator.lower() == 'rtd'):
                num1 = float(input("Enter the angle in radians: "))
    
                print(f"The angle in degrees is: {math.degrees(num1)}")
                continue
    
            #Degrees to Radians
            elif (operator.lower() == 'dtr'):
                num1 = float(input("Enter the angle in degrees: "))
    
                print(f"The angle in radians is: {math.radians(num1)}")
                continue
    
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        #Shapes Calculations
    elif (operator.lower() == 'sc'):
            while True:
                print("""----------------------------------------------------------------
        1.  Triangle -> (tri)
        2.  Circle -> (cir)
        3.  Square -> (sq)
        4.  Rectangle -> (rec)
        5.  Back -> (back)
----------------------------------------------------------------""")
                
                shape = input("Choose a shape: ")

                if (shape.lower() == 'back'):
                    break

                elif (shape not in ['tri', 'cir', 'sq', 'rec']):
                    print("Invalid shape. Please try again.")
                    continue

                try:
                    #Triangle
                    if (shape.lower() == 'tri'):
                        while True:
                            print("""----------------------------------------------------------------
        1.  Area -> (area)
        2.  Perimeter -> (peri)
        3.  Back -> (back)
----------------------------------------------------------------""")
                            
                            sub_operator = input("Choose a operation: ")
    
                            if (sub_operator.lower() == 'back'):
                                break
    
                            elif (sub_operator == 'area'):
                                num1 = input("Enter the base: ")
                                num2 = input("Enter the height: ")
    
                                print(f"The area is: {shapes_formula.area_triangle(num1, num2)}")
                                continue
    
                            elif (sub_operator == 'peri'):
                                num1 = input("Enter the side 1: ")
                                num2 = input("Enter the side 2: ")
                                num3 = input("Enter the side 3: ")
    
                                print(f"The perimeter is: {shapes_formula.perimeter_triangle(num1, num2, num3)}")
                                continue
    
                            else:
                                print("Invalid operation. Please try again.")
                                continue

                    #Circle
                    elif (shape.lower() == 'cir'):
                        while True:
                            print("""----------------------------------------------------------------
        1.  Area -> (area)
        2.  Circumference -> (circ)
        3.  Back -> (back)
----------------------------------------------------------------""")

                            sub_operator = input("Choose a operation: ")
    
                            if (sub_operator.lower() == 'back'):
                                break
    
                            elif (sub_operator == 'area'):
                                num1 = input("Enter the radius: ")
    
                                print(f"The area is: {shapes_formula.area_circle(num1)}")
                                continue

                            elif (sub_operator == 'circ'):
                                num1 = input("Enter the radius: ")

                                print(f"The circumference is: {shapes_formula.circumference_circle(num1)}")
                                continue

                            else:
                                print("Invalid operation. Please try again.")
                                continue

                    #Square
                    elif (shape.lower() == 'sq'):
                        while True:
                            print("""----------------------------------------------------------------
        1.  Area -> (area)
        2.  Perimeter -> (peri)
        3.  Back -> (back)
----------------------------------------------------------------""")
                            
                            sub_operator = input("Choose a operation: ")

                            if (sub_operator.lower() == 'back'):
                                break

                            elif (sub_operator == 'area'):
                                num1 = input("Enter the side: ")

                                print(f"The area is: {shapes_formula.area_square(num1)}")
                                continue

                            elif (sub_operator == 'peri'):
                                num1 = input("Enter the side: ")

                                print(f"The perimeter is: {shapes_formula.perimeter_square(num1)}")
                                continue

                            else:
                                print("Invalid operation. Please try again.")
                                continue

                    #Rectangle
                    elif (shape.lower() == 'rec'):
                        while True:
                            print("""----------------------------------------------------------------
        1.  Area -> (area)
        2.  Perimeter -> (peri)
        3.  Back -> (back)
----------------------------------------------------------------""")
                            
                            sub_operator = input("Choose a operation: ")

                            if (sub_operator.lower() == 'back'):
                                break

                            elif (sub_operator == 'area'):
                                num1 = input("Enter the length: ")
                                num2 = input("Enter the breadth: ")

                                print(f"The area is: {shapes_formula.area_rectangle(num1, num2)}")
                                continue

                            elif (sub_operator == 'peri'):
                                num1 = input("Enter the length: ")
                                num2 = input("Enter the breadth: ")

                                print(f"The perimeter is: {shapes_formula.perimeter_rectangle(num1, num2)}")
                                continue

                            else:
                                print("Invalid operation. Please try again.")
                                continue

                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    continue
    
    else:
        print("Invalid operator. Please try again.")
        continue