#Assignment 2_8: print below output
# 1
# 1 2
# 1 2 3



def printNumber(number):
	for i in range(number):
		for j in range(i+1):
			print(j+1, end= "  ")
		print(" ")		

		

number=int(input("Enter any number: "))

printNumber(number)


