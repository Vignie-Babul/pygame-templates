import sys

import pygame


pygame.init()


screen = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()


is_game_loop = True
while is_game_loop:
	screen.fill('#000000')


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			is_game_loop = False


	pygame.display.flip()
	clock.tick(60)


pygame.quit()
sys.exit()
