import pygame
import random
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, GREY, YELLOW, ALIEN_SHOOTING_SPEED, OFFSET
from game import Game

pygame.init()
pygame.display.set_caption("Python Space Invaders")

# DEFINITIONS

screen = pygame.display.set_mode((SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + 2 * OFFSET))
clock = pygame.time.Clock()

game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET)

# EVENTS

SHOOT_LASER = pygame.USEREVENT
pygame.time.set_timer( SHOOT_LASER, ALIEN_SHOOTING_SPEED )

MYSTERY_SHIP = pygame.USEREVENT + 1
pygame.time.set_timer( MYSTERY_SHIP, random.randint(8000, 12000) )

# GAME LOOP

while True:
    # 1. Event handling
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SHOOT_LASER and game.run:
            game.alien_shoot_laser()

        if event.type == MYSTERY_SHIP and game.run:
            game.create_mystery_ship()
            pygame.time.set_timer( MYSTERY_SHIP, random.randint(8000, 12000) )

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not game.run:
            game.reset()
    
    # 2. Updating positions
    if game.run:
        game.spaceship_group.update()
        game.move_aliens()
        game.alien_lasers_group.update()
        game.mystery_ship_group.update()
        game.check_for_collisions()

    # 3. Drawing objects
    screen.fill(GREY)
    pygame.draw.rect( surface=screen, color=YELLOW, rect=(10,10,780,780), width=2, border_radius=0, border_top_left_radius=60, border_top_right_radius=60, border_bottom_left_radius=60, border_bottom_right_radius=60 )
    pygame.draw.line(screen, YELLOW, (25,730), (775,730), 3)
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
