class Car:
	"""A simple attempt to represent a car"""

	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		"""
		Set the odometer reading to the given value.
		Reject the change if it attempts to roll the odometer back.
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You cannot roll back an odometer")

	def increment_odometer(self, miles):
		self.odometer_reading += miles


class Battery:
	""" A simple attempt to model a battery for an electric Car."""

	def __init__(self, battery_size=75):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print(f"This car has a {self.battery_size}-kWh battery")

	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size == 75:
			range = 260
		elif self.battery == 100:
			range = 315

		print(f"This Car can go about {range} miles on a full charge.")


class ElectricCar(Car):
	""" Represent aspects of a car, specific to eletric vehicles."""

	def __init__(self, make, model, year):
		""" Initialize attributes of the parent class."""
		super().__init__(make, model, year)
		self.battery = Battery()