def build_person(first_name, last_name, age=None):
	"""Return a dictionary of info about a person"""
	personkl = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	return person

musician = build_person('jimi', 'hendrix', 27)
print(musician)