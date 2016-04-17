# coding: utf-8

import os
import pygame
import sys
from pygame.locals import *
from board import Board
from player import Player
import random
pygame.init()
clock = pygame.time.Clock()

### Properties ###
namegame = "Wumpus Game"
screentype = 0
#screentype = FULLSCREEN
sound_volume = 0.4
pygame.display.set_caption(namegame)

### Global variables ###
board = Board()
hunter = Player()
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

def draw_hunter():
	x = (hunter.position_x * board.cell_dimension) + (hunter.position_x * board.spacing) + board.spacing
	y = (hunter.position_y * board.cell_dimension) + (hunter.position_y * board.spacing) + board.spacing
	hunter_image = load_image(hunter.image)
	mainscreen.blit(hunter_image,(x,y))

def draw_matrix():
	x = board.spacing
	y = board.spacing
	
	for i in range (0, len(board.matrix)):
		for j in range (0, len(board.matrix[i])):
			mainscreen.blit(cell,(x,y))
			x += (board.spacing + board.cell_dimension)
		y += (board.spacing + board.cell_dimension)
		x = board.spacing
		
	draw_hunter()
	pygame.display.flip()

def move_left():
	if(hunter.position_x > 0):
		hunter.decrement_x()
		draw_matrix()

def move_right():
	if(hunter.position_x < board.matrix_dimension[1] - 1):
		hunter.increment_x()
		draw_matrix()

def move_up():
	if(hunter.position_y > 0):
		hunter.decrement_y()
		draw_matrix()

def move_down():
	if(hunter.position_y < board.matrix_dimension[0] - 1):
		hunter.increment_y()
		draw_matrix()

def run():
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit(0)
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					move_left()
				elif event.key == pygame.K_RIGHT:
					move_right()
				elif event.key == pygame.K_UP:
					move_up()
				elif event.key == pygame.K_DOWN:
					move_down()
		clock.tick(60)

draw_matrix()
run()
