import pygame
from sprites.player import Player


class GameWorld:
    """
    The point of this class is to keep track of everything. Every character. Every falling object.
    It also keeps track of two-objects colliding together.
    """
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.player = None
        self.falling_sprites = pygame.sprite.Group()

    def add_player(self, player: Player):
        self.all_sprites.add(player)
        self.player = player

    def add_falling_sprite(self, falling_sprite):
        self.all_sprites.add(falling_sprite)
        self.falling_sprites.add(falling_sprite)

    def update(self, dt):
        """
        Updates the game-world by updating every sprite
        :param dt: time in miliseconds
        """
        for sprite in self.all_sprites:
            sprite.update(dt)

    def draw(self, display: pygame.Surface):
        """
        Draws the game-world by drawing every sprite
        """
        for sprite in self.all_sprites:
            sprite.draw(display)
