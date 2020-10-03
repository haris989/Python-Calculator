from time import sleep

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

print("Please select operation -\n"
		"1. Add\n"
		"2. Subtract\n" 
		"3. Multiply\n"
		"4. Divide\n") 


# Taking input from the user 
select = input("Select operations form 1, 2, 3, 4 :") 

number_1 = int(input("Enter first number: ")) 
number_2 = int(input("Enter second number: ")) 

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
	print("Syntax Error!") 
sleep(5) #to show the results for 5 seconds before the program exits!
