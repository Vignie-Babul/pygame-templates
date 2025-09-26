import pygame


pygame.init()


# screen configuration
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption('Base')
clock = pygame.time.Clock()

# main game loop
is_game_loop = True
while is_game_loop:
	# rendering
	# background
	screen.fill('#050505')


	# game events
	for event in pygame.event.get():
		# quit
		if event.type == pygame.QUIT:
			is_game_loop = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				is_game_loop = False


	# display update
	pygame.display.flip()
	clock.tick(60)