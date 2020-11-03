#!/usr/bin/python3

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

operation = input("Enter +,-,*,/ to process: ")

if operation == "+":
	print(x + y)
elif operation == "-":
	print(x - y)
elif operation == "/":
	print(x/y)
elif operation == "*":
	print(x*y)
else:
	print("Your input was incorrect-")
	
