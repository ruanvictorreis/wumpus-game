class Player (object):
	
	def __init__(self):
		self.position_x = 0
		self.position_y = 0
		self.image = "../res/images/hunter/hunter_front.png"
	
	def position(self):
		return (self.x, self.y)
	
	def increment_x(self):
		self.position_x = self.position_x + 1
		self.image = "../res/images/hunter/hunter_right.png"

	def decrement_x(self):
		self.position_x = self.position_x - 1
		self.image = "../res/images/hunter/hunter_left.png"
		
	def increment_y(self):
		self.position_y = self.position_y + 1
		self.image = "../res/images/hunter/hunter_front.png"

	def decrement_y(self):
		self.position_y = self.position_y - 1
		self.image = "../res/images/hunter/hunter_back.png"
