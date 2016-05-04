from PriorityQueue import PriorityQueue
from Cell import Cell

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
        self.srt = '({}, {})'
    
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
        
    def move_a_star(self, goal, board):
        return self.reconstruct_path(self.a_star_search(goal, board), goal)[1]

    def reconstruct_path(self, came_from, goal):
        current = goal
        path = [current]
    
        while current != self:
            current = came_from[current]
            path.append(current)
    
        path.reverse()
        return path

    def neighbors(self, node, board):
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        result = []
        for dir in dirs:
            neighbor = [node.position_x + dir[0], node.position_y + dir[1]]
            if 0 <= neighbor[0] < 6 and 0 <= neighbor[1] < 6 and neighbor not in board.holes_positions and neighbor not \
                    in board.treasure_position:
                result.append(neighbor)
        return result

    def heuristic(self, start, goal):
        dx = abs(start.position_x - goal.position_x)
        dy = abs(start.position_y - goal.position_y)
        return (dx + dy)

    def a_star_search(self , goal, board):
        frontier = PriorityQueue()
        frontier.put(self, 0)

        came_from = {}
        cost_so_far = {}

        came_from[self] = self
        cost_so_far[self] = 0

        while not frontier.empty():
            current = frontier.get()
            if current.position_x == goal.position_x and current.position_y == goal.position_y:
                break

            for next in self.neighbors(current, board):
                next_cell = Cell(next[0], next[1])
                
                if next_cell.position_x == goal.position_x and next_cell.position_y == goal.position_y:
                    next_cell = goal
                new_cost = cost_so_far[current] + self.heuristic(current, next_cell)

                if next_cell not in cost_so_far or new_cost < cost_so_far[next_cell]:
                    cost_so_far[next_cell] = new_cost
                    priority = new_cost + self.heuristic(goal, next_cell)
                    frontier.put(next_cell, priority)
                    came_from[next_cell] = current

        return came_from  # , cost_so_far
