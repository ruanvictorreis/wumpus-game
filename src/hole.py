import math
from random import randint

class Holes (object):	
	def __init__(self):
		self.visible = False
		self.number_holes = 2
		self.holes_position = self.allocate_holes()
		self.brezze_distance = 2
		self.brezze_positions = []
		self.breeze_visible = False
		self.image = "../res/images/hole/hole.png"
		self.breeze = "../res/images/hole/breeze.png"
		
	def allocate_holes(self):
		allocation = []
		allocation_prohibited = [(0,5), (5,0), (4,0), (5,1), (0,4), (1,5)]
		 
		while (len(allocation) < self.number_holes):
			x = randint(0, 5)
			y = randint(0, 5)
			position = (x, y) 
			
			if ((position not in allocation_prohibited) and (position not in allocation)):
				if (len(allocation) != 0):
					add = True
					for allocate in allocation:
						if(abs(x - allocate[0]) == 1 and y == allocate[1]):
							add = False
						if(abs(y - allocate[1]) == 1 and x == allocate[0]):
							add = False
					if(add):
						allocation.append((x, y))			
				else:
					allocation.append((x, y))
		print(allocation)
		return allocation
