#Assignment 2_5: Check whether a number is prime or not

def chkPrime(number):
	divisor=number-1
	while divisor>1:
		if number%divisor==0:
			print("Not Prime")
			exit()
		divisor=divisor-1
	print("Prime number")	
	


number=int(input("Please input number: "))
chkPrime(number)

		
	
	
