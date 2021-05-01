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

#print("Please select operation -\n"
#		"1. Add\n"
#		"2. Subtract\n" 
#		"3. Multiply\n"
#		"4. Divide
#		"\n") 


# Taking input from the user 
#select = input("Select operations form 1, 2, 3, 4 :") 

# Displaying the menu to the user and asking for the input
select = input("""
	Python Calculator

Choose any of the options below :
[1] Add
[2] Subtract
[3] Multiply
[4] Divide

Enter your choice : """)

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
