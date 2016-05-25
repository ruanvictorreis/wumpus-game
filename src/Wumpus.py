from random import randint

from AStar import AStar
from AStar2 import AStar2


class Wumpus(object):
    def __init__(self, board):
        self.visible = False
        self.limit = board.matrix_dimension[1] - 1
        self.initial_position = self.random_position()
        self.position_x = self.initial_position[0]
        self.position_y = self.initial_position[1]
        self.star = AStar(board)
        # self.star = AStar2(board)
        self.smell_distance = 2
        self.smell_positions = []
        self.smell_visible = False
        self.image = "../res/images/wumpus/wumpus.png"
        self.smell = "../res/images/wumpus/smell.png"
        self.srt = '({}, {})'

    def random_position(self):
        x = 0
        y = 0

        while (x <= y):
            x = randint(0, self.limit)
            y = randint(0, self.limit)

        return (x, y)

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
        return self.srt.format(self.position_x, self.position_y)

    def __repr__(self):
        return self.__str__()

    def move_a_star(self, goal):
        return self.star.move(self, goal)
