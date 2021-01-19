twenties=list(range(1, 21))
print(twenties)

million=list(range(1, 1000000))
print(sum(million))

odd_number=list(range(1,20,2))
print(odd_number)

threes=[value * 3 for value in range(3, 31)]
print(threes)

# 4-8
cubes=[value ** 3 for value in range(1, 11)]
for cube in cubes:
	print(cube)