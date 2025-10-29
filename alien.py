import pygame
import random

class Alien(pygame.sprite.Sprite):
    def __init__(self, type: int, x: int, y: int):
        super().__init__()

        self.type = type
        path = f"graphics/alien_{type}.png"
        self.image = pygame.image.load( path )
        self.rect = self.image.get_rect( topleft = (x,y) )

    def update(self, direction: int):
        self.rect.x += direction

class MysteryShip(pygame.sprite.Sprite):
    def __init__(self, screen_width: int):
        super().__init__()

        self.screen_width = screen_width
        self.image = pygame.image.load("graphics/mystery.png")

        x = random.choice([0, screen_width - self.image.get_width()])

        if x == 0:
            self.speed = 3
        else:
            self.speed = -3
        
        self.rect = self.image.get_rect( topleft = (x, 40) )

    def update(self):
        self.rect.x += self.speed

        if self.rect.left > self.screen_width:
            self.kill()
        elif self.rect.right < 0:
            self.kill()