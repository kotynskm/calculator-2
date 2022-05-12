"""CLI application for a prefix-notation calculator."""

# from sys import _enablelegacywindowsfsencoding
from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )



# Replace this with your code

while True:
    user_input = input("Enter a calculation: ")
    tokenize_input = user_input.split(" ")
   
    if tokenize_input[0] == 'q':
        break
    # if input length is < 3, run square function
    if len(tokenize_input) < 3:
        # put square func
        num1 = float(tokenize_input[1])
        print(square(num1))
        break
    try:
        operation = tokenize_input[0]
        num1 = float(tokenize_input[1])
        num2 = float(tokenize_input[2])
    except:
        print("Enter valid input.")
        continue
        # first item = add
    if operation == '+':
            # call the addition function with other 2 args
            # reduce(add, numbers)
        print(add(num1,num2))
    elif operation == '-':
            # call the substraction function with other 2 args   
        print(subtract(num1, num2))
    elif operation == '*':
            # call the multiplication function with other 2 args
        print(multiply(num1, num2))
    elif operation == '/':
            # call the divide function with other 2 args
        print(divide(num1, num2))      
    elif operation == 'square':
            # call the square function with other 2 args
        print(square(num1,)) 
    elif operation == 'cube':
            # call the cube function with other 2 args
        print(cube(num1, num2))
    elif operation == 'pow':
            # call the power function with other 2 args
        print(power(num1, num2))
    elif operation == 'mod':
            # call the modulus function with other 2 args
        print(mod(num1, num2))               