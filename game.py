from typing import List
import pygame
import random
from spaceship import Spaceship
from obstacle import Obstacle
from obstacle import grid
from alien import Alien, MysteryShip
from laser import Laser

class Game:
    def __init__(self, screen_width: int, screen_height: int):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.spaceship_group : pygame.sprite.GroupSingle[Spaceship] = pygame.sprite.GroupSingle() # type: ignore
        self.spaceship_group.add(Spaceship( screen_width=self.screen_width, screen_height=self.screen_height ))
        self.obstacles = self.create_obstacles()
        self.alien_group : pygame.sprite.Group[Alien] = pygame.sprite.Group() # type: ignore
        self.create_aliens()
        self.aliens_direction = 1
        self.alien_lasers_group : pygame.sprite.Group[Laser] = pygame.sprite.Group() # type: ignore
        self.mystery_ship_group = pygame.sprite.GroupSingle()

    def create_obstacles(self) -> List[Obstacle]:
        obstacle_width = len(grid[0]) * 3
        gap = (self.screen_width - (4 * obstacle_width)) / 5

        obstacles = []

        for i in range(4):
            offset_x = int((i + 1) * gap + i * obstacle_width)
            obstacle = Obstacle(offset_x, self.screen_height - 100)
            obstacles.append(obstacle)

        return obstacles
    
    def create_aliens(self):
        for row in range(5):
            for column in range(11):

                x = 75 + column * 55
                y = 110 + row * 55

                if row == 0:
                    alien_type = 3
                elif row in (1,2):
                    alien_type = 2
                else:
                    alien_type = 1
                alien = Alien(alien_type, x, y)
                self.alien_group.add(alien)

    def move_aliens(self):
        self.alien_group.update( self.aliens_direction )

        alien_sprites = self.alien_group.sprites()
        for alien in alien_sprites:
            if alien.rect.right >= self.screen_width:
                self.aliens_direction = -1
                self.alien_move_down(2)
            elif alien.rect.left <= 0:
                self.aliens_direction = 1
                self.alien_move_down(2)

    def alien_move_down(self, distance: int):
        if self.alien_group:
            for alien in self.alien_group.sprites():
                alien.rect.y += distance

    def alien_shoot_laser(self):
        if self.alien_group.sprites():
            random_alien = random.choice( self.alien_group.sprites() )
            laser_sprite = Laser( random_alien.rect.center, -6, self.screen_height )
            self.alien_lasers_group.add(laser_sprite)

    def create_mystery_ship(self):
        self.mystery_ship_group.add(MysteryShip(self.screen_width))

    def check_for_collisions(self):
        # Spaceship
        if self.spaceship_group.sprite.lasers_group:
            for laser_sprite in self.spaceship_group.sprite.lasers_group:
                if pygame.sprite.spritecollide(laser_sprite, self.alien_group, True): # type: ignore
                    laser_sprite.kill()
                if pygame.sprite.spritecollide(laser_sprite, self.mystery_ship_group, True): # type: ignore
                    laser_sprite.kill()

                for obstacle in self.obstacles:
                    if pygame.sprite.spritecollide( laser_sprite, obstacle.blocks_group, True ): # type: ignore
                        laser_sprite.kill()

        # Alien Lasers
        if self.alien_lasers_group:
            for laser_sprite in self.alien_lasers_group:
                if pygame.sprite.spritecollide( laser_sprite, self.spaceship_group, False ): # type: ignore
                    laser_sprite.kill()
                    print("SPACESHIP HIT")
                    
                for obstacle in self.obstacles:
                    if pygame.sprite.spritecollide( laser_sprite, obstacle.blocks_group, True ): # type: ignore
                        laser_sprite.kill()

        if self.alien_group:
            for alien in self.alien_group:
                for obstacle in self.obstacles:
                    pygame.sprite.spritecollide(alien, obstacle.blocks_group, True) # type: ignore
                
                if pygame.sprite.spritecollide( alien, self.spaceship_group, False ): # type: ignore
                    print("SPACESHIP HIT")
