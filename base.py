import pygame

import sys


pygame.init()


# screen configuration
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption('Base')
clock = pygame.time.Clock()


# main game loop
while True:
	# rendering
	# background
	screen.fill('#050505')


	# game events
	for event in pygame.event.get():
		# quit
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()


	# display update
	pygame.display.flip()
	clock.tick(60)