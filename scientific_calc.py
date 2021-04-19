from math import pi, sin, cos, tan, log, factorial, radians


# To get sine of data
def sine(data):
    try:
        return sin(radians(data))  # Converting in radian
    except TypeError:              # Checking for invalid data type
        print('[-] Syntax Error')
    except Exception:
        raise Exception


# cosine of data
def cosine(data):
    try:
        return cos(radians(data))  # Converting in radian
    except TypeError:              # Checking for invalid data type
        print('[-] Syntax Error')
    except Exception:
        raise Exception


# tangent of data
def tangent(data):
    try:
        return tan(radians(data))  # Converting in radian
    except TypeError:              # Checking for invalid data type
        print('[-] Syntax Error')
    except Exception:
        raise Exception


# logarithm of data
def logarithm(data):
    try:
        return log(data)
    except ValueError:              # Checking for invalid data type
        print('[-] Math Error')
    except Exception:
        raise Exception


# Factorial of data
def fact(data):
    try:
        return factorial(int(data))
    except TypeError:              # Checking for invalid data type
        print('[-] Syntax Error')
    except ValueError:              # Checking for invalid data type
        print('[-] Math Error')
    except Exception:
        raise Exception


# prints sci calc main menu, prompts and returns for operation
def print_sci_calc_menu():
    print('''
Sci Calculator:
1. Sine    (sin) 
2. Cosine  (cos)
3. Tangent (tan)
4. Ln     (Natural Log)
5. Factorial (data!)

[*] Note: Please enter angle in degrees 
    ''')
    return input('Select operations form 1, 2, 3, 4, 5 : ')


def sci_operations():
    # Print Menu

    # prompting user to select operation
    select = print_sci_calc_menu()

    data = float(input('Enter data : '))
    if select == '1':
        print(f"sin({data}) = {sine(data)}\n")

    elif select == '2':
        print(f"cos({data}) = {cosine(data)}\n")

    elif select == '3':
        print(f"tan({data}) = {tangent(data)}\n")

    elif select == '4':
        print(f"ln({data}) = {logarithm(data)}\n")

    elif select == '5':
        print(f"{int(data)}! = {fact(data)}\n")

    else:
        print('[-] Syntax Error')
