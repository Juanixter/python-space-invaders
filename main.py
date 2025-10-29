import pygame
import random
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, GREY, ALIEN_SHOOTING_SPEED
from game import Game

pygame.init()
pygame.display.set_caption("Python Space Invaders")

# DEFINITIONS

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)

# EVENTS

SHOOT_LASER = pygame.USEREVENT
pygame.time.set_timer( SHOOT_LASER, ALIEN_SHOOTING_SPEED )

MYSTERY_SHIP = pygame.USEREVENT + 1
pygame.time.set_timer( MYSTERY_SHIP, random.randint(4000, 8000) )

# GAME LOOP

while True:
    # 1. Event handling
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SHOOT_LASER:
            game.alien_shoot_laser()

        if event.type == MYSTERY_SHIP:
            game.create_mystery_ship()
            pygame.time.set_timer( MYSTERY_SHIP, random.randint(4000, 8000) )
    
    # 2. Updating positions
    game.spaceship_group.update()
    game.move_aliens()
    game.alien_lasers_group.update()
    game.mystery_ship_group.update()
    game.check_for_collisions()

    # 3. Drawing objects
    screen.fill(GREY)
    game.spaceship_group.draw( screen )
    game.spaceship_group.sprite.lasers_group.draw( screen )
    for obstacle in game.obstacles:
        obstacle.blocks_group.draw( screen )
    game.alien_group.draw( screen )
    game.alien_lasers_group.draw( screen )
    game.mystery_ship_group.draw( screen )

    # ============================

    pygame.display.update()
    clock.tick(60) # 60 frames/second
