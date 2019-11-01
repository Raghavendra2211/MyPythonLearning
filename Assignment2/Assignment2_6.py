#Assignment 2_6: Print Star as below
# input:5 output: *****
#                 ****
#                 ***
#                 **
#                 *


def printStar(number):
	while number>0:
		for i in range(number):
			print(" * ", end="")
		print(" ")
		number= number-1



number=int(input("Enter any number: "))

printStar(number)


