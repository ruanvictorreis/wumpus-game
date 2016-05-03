class Board(object):
    def __init__(self):
        self.score = 0
        self.spacing = 10
        self.cell_dimension = 100
        self.matrix_dimension = (6, 6)
        self.width = (self.cell_dimension * self.matrix_dimension[1]) + (self.spacing * (self.matrix_dimension[1] + 1))
        self.height = (self.cell_dimension * self.matrix_dimension[0]) + (self.spacing * (self.matrix_dimension[0] + 1))
        self.reserved_positions = [(self.matrix_dimension[0] - 1, 0), (self.matrix_dimension[0] - 2, 0),
                                   (self.matrix_dimension[0] - 1, 1), (0, self.matrix_dimension[1] - 1),
                                   (0, self.matrix_dimension[1] - 2), (1, self.matrix_dimension[1] - 1)]
        self.holes_positions = []
        self.treasure_position = []
