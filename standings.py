import pygame
import lib

class StandingBar(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, city: str, name: str, wins: int, losses: int, ties: int) -> None:
        super().__init__()

        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.SysFont("Courier", 12)

        self.city = self.font.render(city, True, lib.color.BLACK)
        self.name = self.font.render(name, True, lib.color.BLACK)
        self.wins = self.font.render(str(wins), True, lib.color.BLACK)
        self.losses = self.font.render(str(losses), True, lib.color.BLACK)
        self.ties = self.font.render(str(ties), True, lib.color.BLACK)

        self.pos = pygame.math.Vector2(x, y)
        self.image = pygame.Surface([600, 30])
        self.image.fill(lib.color.WHITE)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def draw_stats(self) -> None:
        self.display_surface.blit(self.city, (self.pos.x + 10, self.pos.y + 10))
        self.display_surface.blit(self.name, (self.pos.x + 150, self.pos.y + 10))

        self.display_surface.blit(self.wins, (self.pos.x + 250, self.pos.y + 10))
        self.display_surface.blit(self.losses, (self.pos.x + 280, self.pos.y + 10))
        self.display_surface.blit(self.ties, (self.pos.x + 310, self.pos.y + 10))

    def update(self) -> None:
        self.draw_stats()