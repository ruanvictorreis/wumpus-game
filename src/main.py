# coding: utf-8

import os
import pygame
import sys
from pygame.locals import *
from board import Board
from hunter import Hunter
from wumpus import Wumpus
from random import randint
pygame.init()
clock = pygame.time.Clock()

### Properties ###
namegame = "Wumpus Game"
screentype = 0
#screentype = FULLSCREENs
sound_volume = 0.4
pygame.display.set_caption(namegame)

### Global variables ###
board = Board()
hunter = Hunter()
wumpus = Wumpus()
wumpus.position_x = randint(3,5)
wumpus.position_y = randint(3,5)
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
		
		if(i ==  hunter.smell_distance - 1):
			list_s.append((hunter_x - i, hunter_y - i))
			list_s.append((hunter_x + i, hunter_y + i))
			list_s.append((hunter_x + i, hunter_y - i))
			list_s.append((hunter_x - i, hunter_y + i))
		
		
		for j in list_s:
			if(hunter.smell_visible):
				x = (j[0] * board.cell_dimension) + (j[0] * board.spacing) + board.spacing
				y = (j[1] * board.cell_dimension) + (j[1] * board.spacing) + board.spacing	
				mainscreen.blit(hunter_smell,(x,y))
			hunter_smell_positions.append(j)
				
	hunter.set_small_positions(hunter_smell_positions)

def draw_hunter():
	x = (hunter.position_x * board.cell_dimension) + (hunter.position_x * board.spacing) + board.spacing
	y = (hunter.position_y * board.cell_dimension) + (hunter.position_y * board.spacing) + board.spacing
	hunter_image = load_image_alpha(hunter.image)
	mainscreen.blit(hunter_image,(x,y))
	draw_hunter_smells()
	
def draw_wumpus_smells():
	wumpus_x = wumpus.position_x
	wumpus_y = wumpus.position_y
	wumpus_smell_positions = []
	wumpus.clean_small_positions()
	wumpus_smell = load_image_alpha(wumpus.smell)
	
	for i in range(1, wumpus.smell_distance + 1):
		s1 = (wumpus_x - i, wumpus_y)
		s2 = (wumpus_x + i, wumpus_y)
		s3 = (wumpus_x, wumpus_y - i)         
		s4 = (wumpus_x, wumpus_y + i)
		
		list_s = [s1, s2, s3, s4]
		
		if(i ==  wumpus.smell_distance - 1):
			list_s.append((wumpus_x - i, wumpus_y - i))
			list_s.append((wumpus_x + i, wumpus_y + i))
			list_s.append((wumpus_x + i, wumpus_y - i))
			list_s.append((wumpus_x - i, wumpus_y + i))
		
		for j in list_s:
			if(wumpus.smell_visible):
				x = (j[0] * board.cell_dimension) + (j[0] * board.spacing) + board.spacing
				y = (j[1] * board.cell_dimension) + (j[1] * board.spacing) + board.spacing	
				mainscreen.blit(wumpus_smell,(x,y))
			wumpus_smell_positions.append(j)
				
	wumpus.set_small_positions(wumpus_smell_positions)

def draw_wumpus():
	if(wumpus.visible):	
		x = (wumpus.position_x * board.cell_dimension) + (wumpus.position_x * board.spacing) + board.spacing
		y = (wumpus.position_y * board.cell_dimension) + (wumpus.position_y * board.spacing) + board.spacing
		wumpus_image = load_image(wumpus.image)
		mainscreen.blit(wumpus_image,(x,y))
	draw_wumpus_smells()

def perception_smell(position):
	x = (position[0] * board.cell_dimension) + (position[0] * board.spacing) + board.spacing
	y = (position[1] * board.cell_dimension) + (position[1] * board.spacing) + board.spacing	
	
	wumpus_smell = load_image_alpha(wumpus.smell)
	mainscreen.blit(wumpus_smell,(x,y))

def perception_wumpus(position):
	x = (position[0] * board.cell_dimension) + (position[0] * board.spacing) + board.spacing
	y = (position[1] * board.cell_dimension) + (position[1] * board.spacing) + board.spacing	
	
	wumpus_image = load_image_alpha(wumpus.image)
	mainscreen.blit(wumpus_image,(x,y))

def perception():
	hunter_position = hunter.position()
	smells_position = wumpus.smell_positions
	
	if(hunter_position in smells_position):
		perception_smell(hunter_position)
	
	if(hunter_position == wumpus.position()):
		perception_wumpus(hunter_position)
			
def draw_matrix():
	x = board.spacing
	y = board.spacing
	
	for i in range (0, len(board.matrix)):
		for j in range (0, len(board.matrix[i])):
			mainscreen.blit(cell,(x,y))
			x += (board.spacing + board.cell_dimension)
		y += (board.spacing + board.cell_dimension)
		x = board.spacing
	
	draw_wumpus()
	perception()
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
