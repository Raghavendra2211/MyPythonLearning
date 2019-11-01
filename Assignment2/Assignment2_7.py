#Assignment 2_7: print 1-N,  NxN times


def printNumber(number):
	for i in range(number):
		for j in range(number):
			print( j+1, end=" ")
		print( " ")

		

number=int(input("Enter any number: "))

printNumber(number)


