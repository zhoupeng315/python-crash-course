def describe_pet(pet_name, animal_type='dog'):
	"""Display info about a pet."""
	print(f"\nI have a {animal_type}")
	print(f"My {animal_type}'s name is {pet_name.title()}")

# keywords argument
describe_pet(animal_type='hamster', pet_name = 'harry')
