import random
random.seed(9001)

class MultiSidedDie:
	value = 0

#constructor here
	def __init__(self, number_of_sides):
		self.number_of_sides = number_of_sides


#define method 'roll' to roll the MultiSidedDie
	def roll(self):
		self.value = random.randrange(1, self.number_of_sides)


#define method 'get_value' to return the current value of the MultiSidedDie
	def get_value(self):
		return self.value

#define method 'set_value' to set the die to a particular value
	def set_value(self, value):
	    self.value = value