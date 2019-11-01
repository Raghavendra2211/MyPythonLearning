#Assignment 2_3: Find factorial of a number


def factorial(number):
	fact=1
	while number >0:
		fact=fact*number
		number= number-1
	return fact	



number=int(input("Enter one number: "))

print("Factorial is: ",factorial(number))
