bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0].title())


#last element = -1, -2 = 2nd from the last

print(bicycles[-1], bicycles[-2])


#append new element
bicycles.append('jielante')
print(bicycles)

# insert element
bicycles.insert(0, 'new bike')
print(bicycles)

# remove an element, del
del bicycles[0]
print(bicycles)

# remove element, pop(), remove last element
pop_bicycles = bicycles.pop()
print(bicycles)
print(pop_bicycles)

first_owned = bicycles.pop(0)
print(first_owned)

# remove item by value, only first occurance,, remove()
bicycles.remove('redline')
print(bicycles)

# organize
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# temporary sort
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))
print(cars)
cars.reverse()
print(cars)
print(len(cars))