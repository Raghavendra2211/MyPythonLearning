#Assignment5_2


def printNumber(no):
	if no!=0:
		printNumber(no-1)
		print(no, end="  ")



def main():
	no=int(input("Enter No: "))
	printNumber(no)


if __name__=="__main__":
	main()



