prompt = "\nplease enter your toppings"
prompt += "\n(enter 'quit' when finishes) "

while True:
	message = input(prompt)
	if message == 'quit':
		break
	else:
		print(f"I will add the topping {message}")

