from car import Car, ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_bettle = Car('vw', 'beetle', 2019)
print(my_bettle.get_descriptive_name())