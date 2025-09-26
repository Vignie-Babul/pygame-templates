import pygame

import sys


pygame.init()


def render_fps_counter(master, clock, pos=(4, 4)) -> None:
	fps = round(clock.get_fps())
	font = pygame.font.SysFont('', 20)
	surface = font.render(f'FPS: {fps}', True, '#f2f2f2', None)
	master.blit(surface, pos)


SCREEN_SIZE = (700, 500)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Base')
clock = pygame.time.Clock()


is_game_loop = True
while is_game_loop:
	screen.fill('#050505')
	render_fps_counter(screen, clock)


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			is_game_loop = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				is_game_loop = False


	pygame.display.flip()
	clock.tick(60)
