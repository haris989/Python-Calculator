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

# Square of a number
def square_of_number(num1):
	return num1 * num1

# Cube of number
def cube_of_number(num1):
	return num1 * num1 * num1

print("Please select operation -\n"
		"1. Add\n"
		"2. Subtract\n" 
		"3. Multiply\n"
		"4. Divide\n" 
		"5. Square of Number\n"
		"6. Cube of Number\n") 


# Taking input from the user 
select = input("Select operations form 1, 2, 3, 4,5 :") 

if select == '1':	
	number_1 = int(input("Enter first number: ")) 
	number_2 = int(input("Enter second number: "))  
	print(number_1, "+", number_2, "=", 
					add(number_1, number_2))
	time.sleep(3) #to show the results for 3 seconds before the program exits!

elif select == '2': 
	number_1 = int(input("Enter first number: ")) 
	number_2 = int(input("Enter second number: "))  
	print(number_1, "-", number_2, "=", 
					subtract(number_1, number_2)) 
	time.sleep(3) #to show the results for 3 seconds before the program exits!

elif select == '3': 
	number_1 = int(input("Enter first number: ")) 
	number_2 = int(input("Enter second number: "))  
	print(number_1, "*", number_2, "=", 
					multiply(number_1, number_2)) 
	time.sleep(3) #to show the results for 3 seconds before the program exits!

elif select == '4': 
	number_1 = int(input("Enter first number: ")) 
	number_2 = int(input("Enter second number: "))  
	print(number_1, "/", number_2, "=", 
					divide(number_1, number_2)) 
	time.sleep(3) #to show the results for 3 seconds before the program exits!

elif select == '5': 
	number_1 = int(input("Enter the number: ")) 
	print(number_1, "*", number_1, "=", 
					square_of_number(number_1)) 
	time.sleep(3) #to show the results for 3 seconds before the program exits!

elif select == '6': 
	number_1 = int(input("Enter the number: ")) 
	print(number_1, "*", number_1, "*", number_1, "=", 
					cube_of_number(number_1)) 
	time.sleep(3) #to show the results for 3 seconds before the program exits!

else: 
	print("Syntax Error!") 
	time.sleep(3) #to show the results for 3 seconds before the program exits!
