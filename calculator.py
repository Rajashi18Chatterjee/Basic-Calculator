num_1  = float(input("Enter number 1: "))
num_2 = float(input("Enter number 2: "))
operator = input("Enter the operator you want to perform: ")


if operator == "+":
	print (num_1 + num_2)
elif operator == "-":
	if num_1 > num_2:
		print (num_1 - num_2)
	else:
		print (num_2 - num_1)
elif operator == "*":
	print (num_1 * num_2)
elif operator == "/":
	print(num_1 / num_2)
else:
	print ("The calculator doesn't support this operation.")