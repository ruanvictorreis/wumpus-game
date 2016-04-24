class Wumpus(object):
    def __init__(self, board):
        self.visible = False
        self.position_x = board.matrix_dimension[1] - 1
        self.position_y = 0
        self.smell_distance = 2
        self.smell_positions = []
        self.smell_visible = False
        self.image = "../res/images/wumpus/wumpus.png"
        self.smell = "../res/images/wumpus/smell.png"

    def position(self):
        return self.position_x, self.position_y

    def increment_x(self):
        self.position_x += 1

    def decrement_x(self):
        self.position_x -= 1

    def increment_y(self):
        self.position_y += 1

    def decrement_y(self):
        self.position_y -= 1

    def set_smell_positions(self, positions):
        self.smell_positions = positions

    def clean_smell_positions(self):
        self.smell_positions = []

    def __str__(self):
        return '({}, {})'.format(self.position_x, self.position_y)

    def __repr__(self):
        return self.__str__()
