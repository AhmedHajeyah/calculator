
def main():
	#write your code here
	pass
	FirstNumber= float(input("Enter first number: "))
	SecondNumber= float(input("Enter second number: "))
	operation= input("Choose the operation (+, -, /, *): ")
	if operation == "+":
		sum= FirstNumber + SecondNumber
		print(f"The answer is : {sum}")
	if operation == "-":
		sub= FirstNumber - SecondNumber
		print(f"The answer is : {sub}")
	if operation == "/":
		div= FirstNumber / SecondNumber
		print(f"The answer is : {div}")
	if operation == "*":
		mul= FirstNumber * SecondNumber
		print(f"The answer is : {mul}")
	else: 
		print("Invalid operation")



	


if __name__ == '__main__':
	main()
