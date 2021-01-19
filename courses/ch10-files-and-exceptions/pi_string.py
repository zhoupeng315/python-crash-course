filename = 'pi_million_digits.txt'

pi_string = ''
with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))


birthday = '20170428'
if birthday in pi_string:
	print("your birthday is in pi")
else:
	print("nonono")