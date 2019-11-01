#Assignment 2_9. Find number of digits in input number


def printSum(number):
	sum=1
	while int(number/10) > 0:
		sum=sum+1
		number=int(number/10)
		
	return sum


number=int(input("Input any number: "))

print("Number of digits is :", printSum(number))




	













	








