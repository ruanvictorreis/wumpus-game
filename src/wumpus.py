class Wumpus (object):
	
	def __init__(self):
		self.visible = True
		self.position_x = 5
		self.position_y = 0
		self.smell_distance = 1
		self.smell_positions = []
		self.smell_visible = True
		self.image = "../res/images/wumpus/wumpus.png"
		self.smell = "../res/images/wumpus/smell.png"
		
	def position(self):
		return (self.position_x, self.position_y)
	
	def increment_x(self):
		self.position_x = self.position_x + 1

	def decrement_x(self):
		self.position_x = self.position_x - 1
		
	def increment_y(self):
		self.position_y = self.position_y + 1

	def decrement_y(self):
		self.position_y = self.position_y - 1
	
	def set_small_positions(self, positions):
		self.smell_positions = positions
	
	def clean_small_positions(self):
		self.smell_positions = []
