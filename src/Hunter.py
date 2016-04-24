class Hunter(object):
    def __init__(self, board):
        self.position_x = 0
        self.position_y = board.matrix_dimension[0] - 1
        self.smell_distance = 2
        self.smell_visible = False
        self.smell = "../res/images/hunter/smell.png"
        self.direction = "FRONT"
        self.image = "../res/images/hunter/hunter_front.png"

    def position(self):
        return self.position_x, self.position_y

    def increment_x(self):
        self.image = "../res/images/hunter/hunter_right.png"
        if self.direction == "RIGHT":
            self.position_x += 1
        self.direction = "RIGHT"

    def decrement_x(self):
        self.image = "../res/images/hunter/hunter_left.png"
        if self.direction == "LEFT":
            self.position_x -= 1
        self.direction = "LEFT"

    def increment_y(self):
        self.image = "../res/images/hunter/hunter_front.png"
        if self.direction == "FRONT":
            self.position_y += 1
        self.direction = "FRONT"

    def decrement_y(self):
        self.image = "../res/images/hunter/hunter_back.png"
        if self.direction == "BACK":
            self.position_y -= 1
        self.direction = "BACK"

    def set_small_positions(self, positions):
        self.smell_positions = positions

    def clean_small_positions(self):
        self.smell_positions = []

    def __str__(self):
        return '({}, {})'.format(self.position_x, self.position_y)

    def __repr__(self):
        return self.__str__()
