# coding: utf-8

import sys

import pygame
from Queue import PriorityQueue
from board import Board
from cell import Cell
from hole import Holes
from hunter import Hunter
from treasure import Treasure
from wumpus import Wumpus

pygame.init()
clock = pygame.time.Clock()

### Properties ###
namegame = "Wumpus Game"
screentype = 0
# screentype = FULLSCREEN
sound_volume = 0.4
pygame.display.set_caption(namegame)

### Global variables ###
board = Board()
hunter = Hunter(board)
wumpus = Wumpus(board)
holes = Holes(board)
treasure = Treasure(holes)

mainscreen = pygame.display.set_mode((board.width, board.height), screentype, 32)


###

def load_image_alpha(path):
    imagem = pygame.image.load(path).convert_alpha()
    return imagem


def load_image(path):
    imagem = pygame.image.load(path).convert()
    return imagem


### Global images ###
cell = load_image("../res/images/cell.png")


###

def draw_hunter_smells():
    hunter_x = hunter.position_x
    hunter_y = hunter.position_y
    hunter_smell_positions = []
    hunter.clean_small_positions()
    hunter_smell = load_image_alpha(hunter.smell)

    for i in range(1, hunter.smell_distance + 1):
        s1 = (hunter_x - i, hunter_y)
        s2 = (hunter_x + i, hunter_y)
        s3 = (hunter_x, hunter_y - i)
        s4 = (hunter_x, hunter_y + i)

        list_s = [s1, s2, s3, s4]

        if i == hunter.smell_distance - 1:
            list_s.append((hunter_x - i, hunter_y - i))
            list_s.append((hunter_x + i, hunter_y + i))
            list_s.append((hunter_x + i, hunter_y - i))
            list_s.append((hunter_x - i, hunter_y + i))

        for j in list_s:
            if hunter.smell_visible:
                x = (j[0] * board.cell_dimension) + (j[0] * board.spacing) + board.spacing
                y = (j[1] * board.cell_dimension) + (j[1] * board.spacing) + board.spacing
                mainscreen.blit(hunter_smell, (x, y))
            hunter_smell_positions.append(j)

    hunter.set_small_positions(hunter_smell_positions)


def draw_hunter():
    x = (hunter.position_x * board.cell_dimension) + (hunter.position_x * board.spacing) + board.spacing
    y = (hunter.position_y * board.cell_dimension) + (hunter.position_y * board.spacing) + board.spacing
    hunter_image = load_image_alpha(hunter.image)
    mainscreen.blit(hunter_image, (x, y))
    draw_hunter_smells()


def draw_wumpus_smells():
    wumpus_x = wumpus.position_x
    wumpus_y = wumpus.position_y
    wumpus_smell_positions = []
    wumpus.clean_smell_positions()
    wumpus_smell = load_image_alpha(wumpus.smell)

    for i in range(1, wumpus.smell_distance + 1):
        s1 = (wumpus_x - i, wumpus_y)
        s2 = (wumpus_x + i, wumpus_y)
        s3 = (wumpus_x, wumpus_y - i)
        s4 = (wumpus_x, wumpus_y + i)

        list_s = [s1, s2, s3, s4]

        if i == wumpus.smell_distance - 1:
            list_s.append((wumpus_x - i, wumpus_y - i))
            list_s.append((wumpus_x + i, wumpus_y + i))
            list_s.append((wumpus_x + i, wumpus_y - i))
            list_s.append((wumpus_x - i, wumpus_y + i))

        for j in list_s:
            if wumpus.smell_visible:
                x = (j[0] * board.cell_dimension) + (j[0] * board.spacing) + board.spacing
                y = (j[1] * board.cell_dimension) + (j[1] * board.spacing) + board.spacing
                mainscreen.blit(wumpus_smell, (x, y))
            wumpus_smell_positions.append(j)

    wumpus.set_smell_positions(wumpus_smell_positions)


def draw_wumpus():
    if wumpus.visible:
        x = (wumpus.position_x * board.cell_dimension) + (wumpus.position_x * board.spacing) + board.spacing
        y = (wumpus.position_y * board.cell_dimension) + (wumpus.position_y * board.spacing) + board.spacing
        wumpus_image = load_image(wumpus.image)
        mainscreen.blit(wumpus_image, (x, y))
    draw_wumpus_smells()


def draw_hole_breeze():
    holes_breeze_positions = []
    holes.clean_breeze_positions()
    hole_breeze = load_image_alpha(holes.breeze)

    list_s = []

    for hole in holes.holes_position:
        for i in range(1, holes.breeze_distance + 1):
            hole_x = hole[0]
            hole_y = hole[1]
            list_s.append((hole_x - i, hole_y))
            list_s.append((hole_x + i, hole_y))
            list_s.append((hole_x, hole_y - i))
            list_s.append((hole_x, hole_y + i))

            if i == holes.breeze_distance - 1:
                list_s.append((hole_x - i, hole_y - i))
                list_s.append((hole_x + i, hole_y + i))
                list_s.append((hole_x + i, hole_y - i))
                list_s.append((hole_x - i, hole_y + i))

    for j in list_s:
        if holes.breeze_visible:
            x = (j[0] * board.cell_dimension) + (j[0] * board.spacing) + board.spacing
            y = (j[1] * board.cell_dimension) + (j[1] * board.spacing) + board.spacing
            mainscreen.blit(hole_breeze, (x, y))
        holes_breeze_positions.append(j)
    holes.set_breeze_positions(holes_breeze_positions)


def draw_holes():
    if holes.visible:
        hole_image = load_image(holes.image)
        for position in holes.holes_position:
            x = (position[0] * board.cell_dimension) + (position[0] * board.spacing) + board.spacing
            y = (position[1] * board.cell_dimension) + (position[1] * board.spacing) + board.spacing
            mainscreen.blit(hole_image, (x, y))
    draw_hole_breeze()


def draw_treasure():
    if treasure.visible:
        x = (treasure.position_x * board.cell_dimension) + (treasure.position_x * board.spacing) + board.spacing
        y = (treasure.position_y * board.cell_dimension) + (treasure.position_y * board.spacing) + board.spacing
        treasure_image = load_image_alpha(treasure.image)
        mainscreen.blit(treasure_image, (x, y))


def perception_smell(position):
    x = (position[0] * board.cell_dimension) + (position[0] * board.spacing) + board.spacing
    y = (position[1] * board.cell_dimension) + (position[1] * board.spacing) + board.spacing

    wumpus_smell = load_image_alpha(wumpus.smell)
    mainscreen.blit(wumpus_smell, (x, y))


def perception_wumpus(position):
    x = (position[0] * board.cell_dimension) + (position[0] * board.spacing) + board.spacing
    y = (position[1] * board.cell_dimension) + (position[1] * board.spacing) + board.spacing

    wumpus_image = load_image_alpha(wumpus.image)
    mainscreen.blit(wumpus_image, (x, y))


def perception_treasure(position):
    x = (position[0] * board.cell_dimension) + (position[0] * board.spacing) + board.spacing
    y = (position[1] * board.cell_dimension) + (position[1] * board.spacing) + board.spacing

    treasure_image = load_image_alpha(treasure.image)
    mainscreen.blit(treasure_image, (x, y))


def perception_breeze(position):
    x = (position[0] * board.cell_dimension) + (position[0] * board.spacing) + board.spacing
    y = (position[1] * board.cell_dimension) + (position[1] * board.spacing) + board.spacing

    breeze_image = load_image_alpha(holes.breeze)
    mainscreen.blit(breeze_image, (x, y))


def perception_holes(position):
    x = (position[0] * board.cell_dimension) + (position[0] * board.spacing) + board.spacing
    y = (position[1] * board.cell_dimension) + (position[1] * board.spacing) + board.spacing

    holes_image = load_image_alpha(holes.image)
    mainscreen.blit(holes_image, (x, y))


def perception():
    hunter_position = hunter.position()
    smells_position = wumpus.smell_positions
    breezes_position = holes.breeze_positions

    if hunter_position == wumpus.position():
        perception_wumpus(hunter_position)

    if hunter_position == treasure.position:
        perception_treasure(hunter_position)

    if hunter_position in smells_position:
        perception_smell(hunter_position)

    if hunter_position in breezes_position:
        perception_breeze(hunter_position)

    if hunter_position in holes.holes_position:
        perception_holes(hunter_position)


def draw_matrix():
    x = board.spacing
    y = board.spacing

    for i in range(0, board.matrix_dimension[0]):
        for j in range(0, board.matrix_dimension[1]):
            mainscreen.blit(cell, (x, y))
            x += (board.spacing + board.cell_dimension)
        y += (board.spacing + board.cell_dimension)
        x = board.spacing

    draw_holes()
    draw_wumpus()
    draw_treasure()
    perception()
    draw_hunter()
    pygame.display.flip()


def hunter_move_left():
    if hunter.position_x > 0:
        hunter.decrement_x()
        draw_matrix()


def hunter_move_right():
    if hunter.position_x < board.matrix_dimension[1] - 1:
        hunter.increment_x()
        draw_matrix()


def hunter_move_up():
    if hunter.position_y > 0:
        hunter.decrement_y()
        draw_matrix()


def hunter_move_down():
    if hunter.position_y < board.matrix_dimension[0] - 1:
        hunter.increment_y()
        draw_matrix()


def wumpus_move_left():
    if wumpus.position_x > 0:
        wumpus.decrement_x()
        draw_matrix()


def wumpus_move_right():
    if wumpus.position_x < board.matrix_dimension[1] - 1:
        wumpus.increment_x()
        draw_matrix()


def wumpus_move_up():
    if wumpus.position_y > 0:
        wumpus.decrement_y()
        draw_matrix()


def wumpus_move_down():
    if wumpus.position_y < board.matrix_dimension[0] - 1:
        wumpus.increment_y()
        draw_matrix()


def heuristic(start, goal):
    dx = abs(start.position_x - goal.position_x)
    dy = abs(start.position_y - goal.position_y)
    return (dx + dy)


def a_star_search(start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)

    came_from = {}
    cost_so_far = {}

    came_from[start] = start
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()
        if current.position_x == goal.position_x and current.position_y == goal.position_y:
            print('WUMPUS FOUND HUNTER... Done!')
            break

        for next in neighbors(current):
            next_cell = Cell(next[0], next[1])
            new_cost = cost_so_far[current] + heuristic(current, next_cell)
            if next_cell not in cost_so_far or new_cost < cost_so_far[next_cell]:
                cost_so_far[next_cell] = new_cost
                priority = new_cost + heuristic(goal, next_cell)
                frontier.put(next_cell, priority)
                came_from[next_cell] = current

    return came_from, cost_so_far


def neighbors(node):
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    result = []
    for dir in dirs:
        neighbor = [node.position_x + dir[0], node.position_y + dir[1]]
        if 0 <= neighbor[0] < 6 and 0 <= neighbor[1] < 6:
            result.append(neighbor)
    return result


def run():
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    hunter_move_left()
                    result = a_star_search(wumpus, hunter)
                    for x in result:
                        print(x)
                elif event.key == pygame.K_RIGHT:
                    hunter_move_right()
                    a_star_search(wumpus, hunter)
                elif event.key == pygame.K_UP:
                    hunter_move_up()
                    a_star_search(wumpus, hunter)
                elif event.key == pygame.K_DOWN:
                    hunter_move_down()
                    a_star_search(wumpus, hunter)
        clock.tick(60)


draw_matrix()
run()
