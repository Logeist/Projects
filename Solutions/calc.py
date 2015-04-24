def main():
	a = float(input("Enter your first term: "))
	b = float(input("Enter your second term: "))
	op = input("Enter your operation (valid: + - * /): ")
	for i in op:
		if i == '+':
			result = a + b
			print(result)
		elif i == '-':
			result = a - b
			print(result)
		elif i == '*':
			result = a * b
			print(result)
		elif i == '/':
			result = a / b
			print(result)
		else:
			print("Invalid operation!")




if __name__ == "__main__":
    main()