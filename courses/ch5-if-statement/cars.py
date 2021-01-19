cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())


age_0 = 22
age_1 = 18

print(age_1 >= 21 or age_0 >= 21)


#check whether value is in the list

print('bmw' in cars)
