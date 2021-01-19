# try:
# 	print(5/0)
# except ZeroDivisionError:
# 	print("you can't divide by zero!")

print("give me 2 numbers, and I will divide them")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst Number:")
	if first_number == 'q':
		break
	second_number = input("Second Number:")
	if second_number == 'q':
		break
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You cant divide by 0")
	else:
		print(answer)