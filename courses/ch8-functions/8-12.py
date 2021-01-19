def build_sandwitch(*items):
	"""build sanwitch"""
	print("items received to make sanwitch")
	for item in items:
		print(f"\t{item}")

build_sandwitch('cucumber')
build_sandwitch('tomato', 'meat', 'sauce')


def build_profile(first, last, **kwargs):
	kwargs['first'] = first
	kwargs['last'] = last
	print(kwargs)

build_profile('eric', 'zhou', like='wife', fav='kid')

