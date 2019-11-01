#Assignment 2_10. Find Sum of digits in input number


def printSum(number):
	sum=0
	while int(number/10) > 0:
		sum=sum+number%10
		number=int(number/10)
	sum=sum+number%10	
	return sum


number=int(input("Input any number: "))

print("Sum of digits is :", printSum(number))




	








