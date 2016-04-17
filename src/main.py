# coding: utf-8

import os
import pygame
import sys
from pygame.locals import *
import random
pygame.init()
clock = pygame.time.Clock()

### Properties ###
namegame = "Wumpus Game"
width = 1280
height = 720
screentype = 0
#screentype = FULLSCREEN
sound_volume = 0.4

### Global variables ###
mainscreen = pygame.display.set_mode((width, height), screentype, 32)
###

def load_image_alpha(path):
	imagem = pygame.image.load(path).convert_alpha()
	return imagem

def load_image(path):
	imagem = pygame.image.load(path).convert()
	return imagem

### Global Images ###

