#Assignment5_5

fac=1
def factorial(no):
	if no==0:
		return 1
	else:
		global fac
		if no!=1:
			fac=fac*no
			factorial(no-1)
		return fac


def main():
	no=int(input("Enter No: "))
	print("Factorial is ",factorial(no))


if __name__=="__main__":
	main()



