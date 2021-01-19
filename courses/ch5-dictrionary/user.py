user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
}

for key, value in user_0.items():
	print(f"\nKey: {key}")
	print(f"Value: {value}")
	print(f"Value: {user_0[key]}")

# .key() is optional, 
for k in user_0.keys():
	print(k)

for k in user_0:
	print(k)


favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}

for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking the poll")


# use set to make unique
for language in set(favorite_languages.values()):
	print(language)