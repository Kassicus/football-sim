import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Color():
    def __init__(self) -> None:
        self.BLACK = pygame.Color(0, 0, 0, 255)
        self.WHITE = pygame.Color(255, 255, 255, 255)

color = Color()

display_surface = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
events = pygame.event.get()
delta_time = 0
fps_limit = 120