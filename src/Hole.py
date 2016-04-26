from random import randint


class Holes(object):
    def __init__(self, board):
        self.board = board
        self.visible = True
        self.number_holes = 6
        self.holes_position = self.allocate_holes()
        self.breeze_distance = 1
        self.breeze_positions = []
        self.breeze_visible = True
        self.image = "../res/images/hole/hole.png"
        self.breeze = "../res/images/hole/breeze.png"

    def allocate_holes(self):
        allocation = []

        while len(allocation) < self.number_holes:
            x = randint(0, self.board.matrix_dimension[1] - 1)
            y = randint(0, self.board.matrix_dimension[0] - 1)
            position = (x, y)

            if (position not in self.board.reserved_positions) and (position not in allocation):
                if len(allocation) != 0:
                    add = True
                    for allocate in allocation:
                        if abs(x - allocate[0]) == 1 and y == allocate[1]:
                            add = False
                        if abs(y - allocate[1]) == 1 and x == allocate[0]:
                            add = False
                    if add:
                        allocation.append((x, y))
                        self.board.holes_positions.append([x, y])
                else:
                    allocation.append((x, y))
                    self.board.holes_positions.append([x, y])
        return allocation

    def set_breeze_positions(self, positions):
        self.breeze_positions = positions

    def clean_breeze_positions(self):
        self.breeze_positions = []
