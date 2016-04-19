import math
from random import randint

class Treasure (object):	
	def __init__(self, holes):
		self.visible = False
		self.holes = holes
		self.board = holes.board
		self.position = self.allocate_treasure()
		self.position_x = self.position[0]
		self.position_y = self.position[1]
		self.image = "../res/images/treasure/treasure.png"
	
	def allocate_treasure(self):
		position = None
		while (position == None):
			x = randint(0, self.board.matrix_dimension[1] - 1)
			y = randint(0, self.board.matrix_dimension[0] - 1)
			temp = (x, y) 
			
			if ((temp not in self.board.reserved_positions) and (temp not in self.holes.holes_position)):
				position = temp
		return position
