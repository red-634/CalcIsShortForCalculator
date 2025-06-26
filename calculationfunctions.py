import math

def add(num1, num2):
    #Add two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    sumans = num1 + num2
    print(f"The sum of {num1} and {num2} is {sumans}")

def subtract(num1, num2):
    #Subtract two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    differenceans = num1 - num2
    print(f"The difference between {num1} and {num2} is {differenceans}")

def multiply():
    #Multiply numbers
    numbers = input("Enter numbers to multiply, separated by spaces: ").split()
    product = 1
    for num in numbers:
        productans *= float(num)
    print(f"The product of {', '.join(numbers)} is {productans}")

def divide(num1, num2):
    #Divide two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        quotient = num1 / num2
        print(f"The quotient of {num1} divided by {num2} is {quotient}")

def power(base, exponent):
    #Calculate the power of a number
    base = float(input("Enter the base: "))
    exponent = float(input("Enter the exponent: "))
    powerans = base ** exponent
    print(f"{base} raised to the power of {exponent} is {powerans}")

def square_root(num):
    #Calculate the square root of a number
    num = float(input("Enter a number to find its square root: "))
    if num < 0:
        print("Error: Cannot calculate the square root of a negative number.")
    else:
        sqrtans = math.sqrt(num)
        print(f"The square root of {num} is {sqrtans}")

def cube_root(num):
    #Calculate the cube root of a number
    num = float(input("Enter a number to find its cube root: "))
    cuberootans = num ** (1/3)
    print(f"The cube root of {num} is {cuberootans}")

def log(num, base):
    #Calculate the logarithm of a number
    num = float(input("Enter the number to find its logarithm: "))
    base = float(input("Enter the base for the logarithm: "))
    if num <= 0 or base <= 0 or base == 1:
        print("Error: Invalid input for logarithm.")
    else:
        logans = math.log(num, base)
        print(f"The logarithm of {num} to the base {base} is {logans}")

def cosine(angle):
    #Calculate the cosine of an angle
    input("Do you want to calculate in radians or degrees? (r/d):")
    if input.lower() == 'r':
        angle = float(input("Enter the angle in radians: "))
        cosineans = math.cos(angle)
        print(f"The cosine of {angle} radians is {cosineans}")  
    elif input.lower() == 'd':
        angle = float(input("Enter the angle in degrees: "))
        radians = math.radians(angle)
        cosineans = math.cos(radians)
        print(f"The cosine of {angle} degrees is {cosineans}")
    else:
        print("Invalid input. Please enter 'r' for radians or 'd' for degrees.")
        cosine (angle)

def sine(angle):
    #Calculate the sine of an angle
    input("Do you want to calculate in radians or degrees? (r/d):")
    if input.lower() == 'r':
        angle = float(input("Enter the angle in radians: "))
        sineans = math.sin(angle)
        print(f"The sine of {angle} radians is {sineans}")  
    elif input.lower() == 'd':
        angle = float(input("Enter the angle in degrees: "))
        radians = math.radians(angle)
        sineans = math.sin(radians)
        print(f"The sine of {angle} degrees is {sineans}")
    else:
        print("Invalid input. Please enter 'r' for radians or 'd' for degrees.")
        sine(angle)

def tangent(angle):
    #Calculate the tangent of an angle
    input("Do you want to calculate in radians or degrees? (r/d):")
    if input.lower() == 'r':
        angle = float(input("Enter the angle in radians: "))
        tangentans = math.tan(angle)
        print(f"The tangent of {angle} radians is {tangentans}")  
    elif input.lower() == 'd':
        angle = float(input("Enter the angle in degrees: "))
        radians = math.radians(angle)
        tangentans = math.tan(radians)
        print(f"The tangent of {angle} degrees is {tangentans}")
    else:
        print("Invalid input. Please enter 'r' for radians or 'd' for degrees.")
        tangent(angle)

def inverse_cosine(value):
    #Calculate the inverse cosine (arccos) of a value
    value = float(input("Enter a value for inverse cosine: "))
    if value < -1 or value > 1:
        print("Error: Value must be between -1 and 1.")
    else:
        arccosans = math.acos(value)
        print(f"The inverse cosine of {value} is {arccosans} radians.")

def inverse_sine(value):
    #Calculate the inverse sine (arcsin) of a value
    value = float(input("Enter a value for inverse sine: "))
    if value < -1 or value > 1:
        print("Error: Value must be between -1 and 1.")
    else:
        arcsinans = math.asin(value)
        print(f"The inverse sine of {value} is {arcsinans} radians.")

def inverse_tangent(value):
    #Calculate the inverse tangent (arctan) of a value
    value = float(input("Enter a value for inverse tangent: "))
    arctanans = math.atan(value)
    print(f"The inverse tangent of {value} is {arctanans} radians.")