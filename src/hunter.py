class Hunter (object):
	
	def __init__(self):
		self.position_x = 0
		self.position_y = 0
		self.smell_distance = 2
		self.smell_visible = True
		self.smell = "../res/images/hunter/smell.png"
		self.direction = "FRONT"
		self.image = "../res/images/hunter/hunter_front.png"
	
	def position(self):
		return (self.x, self.y)
	
	def increment_x(self):
		self.image = "../res/images/hunter/hunter_right.png"
		if(self.direction == "RIGHT"):
			self.position_x = self.position_x + 1
		self.direction = "RIGHT"

	def decrement_x(self):
		self.image = "../res/images/hunter/hunter_left.png"
		if(self.direction == "LEFT"):
			self.position_x = self.position_x - 1
		self.direction = "LEFT"
		
	def increment_y(self):
		self.image = "../res/images/hunter/hunter_front.png"
		if(self.direction == "FRONT"):
			self.position_y = self.position_y + 1
		self.direction = "FRONT"

	def decrement_y(self):
		self.image = "../res/images/hunter/hunter_back.png"
		if(self.direction == "BACK"):
			self.position_y = self.position_y - 1
		self.direction = "BACK"
		
	def set_small_positions(self, positions):
		self.smell_positions.append(positions)
		
	def clean_small_positions(self):
		self.smell_positions = []
