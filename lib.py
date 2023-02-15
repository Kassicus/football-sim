import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Color():
    def __init__(self) -> None:
        self.BLACK = pygame.Color(0, 0, 0, 255)
        self.WHITE = pygame.Color(255, 255, 255, 255)

    def get_random_color(self) -> pygame.Color:
        color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        return color

color = Color()

display_surface = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
events = pygame.event.get()
delta_time = 0
fps_limit = 120