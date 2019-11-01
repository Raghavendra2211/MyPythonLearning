#Assignment 2_4: Sum of factors of a number



def sumOfFactors(number):
	n=number-1
	sum=1
	
	while (n>1):
		if number%n == 0:
			sum=sum+n
		n=n-1

	return sum



number=int(input("Please enter any number: "))

print(sumOfFactors(number))

