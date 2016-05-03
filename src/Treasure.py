from random import randint


class Treasure(object):
    def __init__(self, holes):
        self.visible = True
        self.holes = holes
        self.board = holes.board
        self.position = self.allocate_treasure()
        self.position_x = self.position[0]
        self.position_y = self.position[1]
        self.image = "../res/images/treasure/treasure.png"

    def allocate_treasure(self):
        position = None
        while position is None:
            x = randint(0, self.board.matrix_dimension[1] - 1)
            y = randint(0, self.board.matrix_dimension[0] - 1)
            temp = (x, y)

            if (temp not in self.board.reserved_positions) and (temp not in self.holes.holes_position):
                position = temp
        self.board.treasure_position.append([x, y])
        return position

    def __str__(self):
        return '({}, {})'.format(self.position_x, self.position_y)

    def __repr__(self):
        return self.__str__()
