import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, GREY
from game import Game

pygame.init()
pygame.display.set_caption("Python Space Invaders")

# DEFINITIONS

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)

# GAME LOOP

while True:
    # 1. Event handling
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # 2. Updating positions
    game.spaceship_group.update()

    # 3. Drawing objects
    screen.fill(GREY)
    game.spaceship_group.draw( screen )
    game.spaceship_group.sprite.lasers_group.draw( screen )
    for obstacle in game.obstacles:
        obstacle.blocks_group.draw( screen )

    # ============================

    pygame.display.update()
    clock.tick(60) # 60 frames/second
