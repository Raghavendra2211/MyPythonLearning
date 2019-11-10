#Assignment5_3


def printStar(no):
	if no!=0:
		print(no, end="  ")
		printStar(no-1)
		

def main():
	no=int(input("Enter No: "))
	printStar(no)


if __name__=="__main__":
	main()



