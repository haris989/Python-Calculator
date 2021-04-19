import time
from scientific_calc import *


# add two numbers
def add(num1, num2):
    return num1 + num2


# subtract two numbers
def subtract(num1, num2):
    return num1 - num2


# multiply two numbers
def multiply(num1, num2):
    return num1 * num2


# divide two numbers
def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print('[-] Math Error : Cannot Divide by 0 ')
        return float('inf')


# adding new option for scientific calculations
print(
    '''Please select operation -
1. Add
2. Subtract
3. Multiply
4. Divide
5. Scientific Calc
''')


# # Taking input from the user
select = input("Select operations form 1, 2, 3, 4 ,5: ")

if select == '5':
    sci_operations()

else:
    number_1 = float(input("Enter first number: "))
    number_2 = float(input("Enter second number: "))

    if select == '1':
        print(number_1, "+", number_2, "=",
              add(number_1, number_2))

    elif select == '2':
        print(number_1, "-", number_2, "=",
              subtract(number_1, number_2))

    elif select == '3':
        print(number_1, "*", number_2, "=",
              multiply(number_1, number_2))

    elif select == '4':
        print(number_1, "/", number_2, "=",
              divide(number_1, number_2))

    else:
        print("[-] Syntax Error!")

time.sleep(3)  # to show the results for 3 seconds before the program exits!
