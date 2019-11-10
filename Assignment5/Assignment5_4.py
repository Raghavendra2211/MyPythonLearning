#Assignment5_4

sum=0

def sumofdigits(no):
	global sum
	if no==0:
		return sum
	else:
		sum=sum+no%10
		sumofdigits(no//10)
		return sum


def main():
	no=int(input("Enter No: "))
	print("Sum of digit is ",sumofdigits(no))
	
	
	
if __name__=="__main__":
	main()



