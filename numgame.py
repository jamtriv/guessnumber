import random
from pygame.locals import *
from sys import exit
import pygame
from enum import Enum
from random import randint

#tiktok
clock=pygame.time.Clock()

user = int(input("Please enter a number!"))
computer = randint(0,20)


#setup the display
pygame.init()
screen_width=800
screen_length=600
screen = pygame.display.set_mode((screen_width, screen_length))

while True:
    clock.tick(30)
