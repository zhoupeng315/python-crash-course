filename = 'pi_digits.txt'

with open(filename) as file_object:
	# content = file_object.read()
	for line in file_object:
		print(line.rstrip())
	
# print("content:",content)

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.strip()

print(pi_string)