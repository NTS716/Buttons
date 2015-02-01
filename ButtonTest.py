import pygame
from pygame.locals import *
import sys
from Buttons import *

#Initialize Pygame
pygame.init()

#Setup the display
SCREEN = pygame.display.set_mode((800,600))

#Create clock object
clock = pygame.time.Clock()

#Create the buttons
rectButton = Button(SCREEN, 'rect', (100, 100), (200, 150), (255,255,255))
imgButton = Button(SCREEN, 'img', (300, 300), (100, 100), ('button.png'))

#Event loop
while True:
	#Fill the screen with black
	SCREEN.fill((0,0,0))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		#if the image is clicked, quit
		elif event.type == MOUSEBUTTONDOWN:
			if imgButton.touching(pygame.mouse.get_pos()):
				pygame.quit()
				sys.exit()
	#Put the buttons on the screen
	rectButton.draw()
	imgButton.draw()
	#Puts text on the rect
	rectButton.addText('Hi', 'courier', 30, (0, 0, 0), 10)
	#Puts a border around the rect
	rectButton.bevel((0, 255, 0), 5, ['all'])
	#if the mouse goes over the rect, the rect changes
	if rectButton.touching(pygame.mouse.get_pos()):
		rectButton.detail = (255, 0, 0)
	else:
		rectButton.detail = (255, 255, 255)
	pygame.display.update()
	clock.tick(60)
