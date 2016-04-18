class Board (object):
	
	def __init__(self):
		self.score = 0
		self.spacing = 10
		self.cell_dimension = 100
		self.matrix_dimension = (4,4)
		self.width = (self.cell_dimension * self.matrix_dimension[1]) + (self.spacing * (self.matrix_dimension[1] + 1) )
		self.height = (self.cell_dimension * self.matrix_dimension[0]) + (self.spacing * (self.matrix_dimension[0] + 1) )
		

