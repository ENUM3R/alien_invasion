import pygame


class Ship:
    def __init__(self, al_game):
        self.screen = al_game.screen
        self.settings = al_game.settings
        self.screen_rect = al_game.screen.get_rect()

        self.image = pygame.image.load('C:\\Users\\cypri\\PycharmProjects\\alien_invasion\\shipVer.bmp')
        self.image = pygame.transform.smoothscale(self.image, (45, 45))
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        self.y = float(self.rect.y)
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.settings.screen_height:
            self.rect.y += self.settings.ship_speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)
