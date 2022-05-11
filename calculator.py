"""CLI application for a prefix-notation calculator."""

# from sys import _enablelegacywindowsfsencoding
from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

while True:
    user_input = input("Enter a calculation: ")
    tokenize_input = user_input.split(" ")
    operation = tokenize_input[0]
    num1 = int(tokenize_input[1])
    num2 = int(tokenize_input[2])
    if operation == 'q':
        break
    else:
        # first item = add
        if operation == '+':
            # call the addition function with other 2 args
            print(add(num1,num2))
        elif operation == '-':
            # call the substraction function with other 2 args   
            print(subtract(num1, num2))
        elif operation == '*':
            # call the multiplication function with other 2 args
            print(multiply(num1, num2)) 
