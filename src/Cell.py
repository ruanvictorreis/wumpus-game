class Cell(object):
    def __init__(self, x, y):
        self.position_x = x
        self.position_y = y

    def __str__(self):
        return '({}, {})'.format(self.position_x, self.position_y)

    def __repr__(self):
        return self.__str__()

    def position(self):
        return self.position_x, self.position_y
