cat_file = 'cats.txt'

try:
	with open(cat_file) as f:
		contents = f.read()
except FileNotFoundError:
	print("cat file not exist")
else:
	cats = contents.split()
	for cat in cats:
		print(cat)