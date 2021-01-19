from random import randint

class Dice:
	"""random dice from 1 - 6"""
	def __init__(self):
		self.sides = 6

	def roll_die(self):
		self.sides = randint(1, 6)
		print(f"Dice sides = {self.sides}")



my_dice = Dice()

for i in range(1, 11):
	my_dice.roll_die()