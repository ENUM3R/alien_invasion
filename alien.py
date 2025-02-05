import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, al_game):
        super().__init__()
        self.screen = al_game.screen
        self.screen_rect = al_game.screen.get_rect()

        self.image = pygame.image.load('C:\\Users\\cypri\\PycharmProjects\\alien_invasion\\alien.bmp')
        self.image = pygame.transform.smoothscale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        self.rect.right = self.screen_rect.right
        self.rect.y = 0

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
