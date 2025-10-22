import pygame
import sys

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, GREY
from spaceship import Spaceship

pygame.init()
pygame.display.set_caption("Python Space Invaders")

# DEFINITIONS

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

spaceship = Spaceship( screen_width = SCREEN_WIDTH, screen_height = SCREEN_HEIGHT )
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

# GAME LOOP

while True:
    # 1. Event handling
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # 2. Updating positions

    spaceship_group.update()

    # 3. Drawing objects

    screen.fill(GREY)
    spaceship_group.draw(screen)

    # ============================

    pygame.display.update()
    clock.tick(60) # 60 frames/second
