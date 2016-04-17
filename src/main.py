# coding: utf-8

import os
import pygame
import sys
from pygame.locals import *
from board import Board
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

def draw_matrix():
	x = board.spacing
	y = board.spacing
	
	for i in range (0, len(board.matrix)):
		for j in range (0, len(board.matrix[i])):
			mainscreen.blit(cell,(x,y))
			x += (board.spacing + board.cell_dimension)
		y += (board.spacing + board.cell_dimension)
		x = board.spacing
	pygame.display.flip()

def run():
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit(0)
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					continue
				elif event.key == pygame.K_RIGHT:
					continue
		clock.tick(60)
draw_matrix()
run()
