from PriorityQueue import PriorityQueue
from Cell import Cell

class AStar(object):
    def __init__(self, board):
		self.board = board

    def move(self, start, goal):
        return self.reconstruct_path(self.a_star_search(start, goal), start, goal)[1]
   
    def reconstruct_path(self, came_from, start, goal):
        current = goal
        path = [current]
    
        while current != start:
            current = came_from[current]
            path.append(current)
    
        path.reverse()
        return path

    def neighbors(self, node):
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        result = []
        for dir in dirs:
            neighbor = [node.position_x + dir[0], node.position_y + dir[1]]
            if 0 <= neighbor[0] < self.board.matrix_dimension[0] and 0 <= neighbor[1] < 6 \
                and neighbor not in self.board.holes_positions and neighbor not \
                    in self.board.treasure_position:
                result.append(neighbor)
        return result

    def heuristic(self, start, goal):
        dx = abs(start.position_x - goal.position_x)
        dy = abs(start.position_y - goal.position_y)
        return (dx + dy)

    def a_star_search(self , start, goal):
        frontier = PriorityQueue()
        frontier.put(start, 0)

        came_from = {}
        cost_so_far = {}

        came_from[start] = start
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.get()
            if current.position_x == goal.position_x and current.position_y == goal.position_y:
                break

            for next in self.neighbors(current):
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

