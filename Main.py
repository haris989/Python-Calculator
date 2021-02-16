import time

#add two numbers 
def add(num1, num2): 
	return num1 + num2 

#subtract two numbers 
def subtract(num1, num2): 
	return num1 - num2 

#multiply two numbers 
def multiply(num1, num2): 
	return num1 * num2 

#divide two numbers 
def divide(num1, num2): 
	return num1 / num2 
#Factorial of a number
def fact(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s;
    
print("Please select operation -\n"
		"1. Add\n"
		"2. Subtract\n" 
		"3. Multiply\n"
		"4. Divide\n"
		"5. Factorial\n") 


# Taking input from the user 
select = input("Select operations ranging form 1, 2, 3, 4, 5 :")
if select == '5':
    n = int(input("Enter the desired number: "))
    print(n,'! = ', fact(n))
    time.sleep(5)
else:    
    number_1 = int(input("Enter first number: ")) 
    number_2 = int(input("Enter second number: ")) 

    if select == '1': 
	    print(number_1, "+", number_2, "=", 
					add(number_1, number_2))
	    time.sleep(5) #to show the results for 5 seconds before the program exits!

    elif select == '2': 
	    print(number_1, "-", number_2, "=", 
					subtract(number_1, number_2)) 
	    time.sleep(5) #to show the results for 5 seconds before the program exits!

    elif select == '3': 
	    print(number_1, "*", number_2, "=", 
					multiply(number_1, number_2)) 
	    time.sleep(5) #to show the results for 5 seconds before the program exits!

    elif select == '4': 
	    print(number_1, "/", number_2, "=", 
					divide(number_1, number_2)) 
	    time.sleep(5) #to show the results for 5 seconds before the program exits!
    else: 
	    print("Syntax Error!") 
	    time.sleep(5) #to show the results for 5 seconds before the program exits!
