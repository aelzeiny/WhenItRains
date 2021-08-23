import pygame
from typing import List

from sprites.anim import Animation


PLAYER_WIDTH = 72
PLAYER_HEIGHT = 120
VELO_X = .2  # PIXELS PER MS

ANIM_IDLE = 0
ANIM_RUNNING = 1

STATE_IDLE = 0
STATE_RUNNING = 1


class Player(pygame.sprite.Sprite):
    """
    Hey JB. Welcome to classes, and also inheritance!
    A Player is a thing with a lot of variables that are unique to it: like animation, X pos, Y pos.
    That's what we call 'state'. Unfortunately, a function does not hold state. So we need another tool that does,
    like classes!

    For example, we can create 2 Players like at coordiantes (0, 0) and (0, 100)
    a = Player(0, 0)
    b = Player(0, 100)

    and we can get the X position like
    player_a_x = a.x

    and we can call functions that do things to the player like
    player.stand_still()
    player.run_left()
    player.run_right()
    player.update(.01)
    """

    def __init__(self, x: float, y: float):
        super().__init__()  # This line means call the __init__ of the Sprite class
        self.animations = self._load_anims()
        # we set this value to 0 to start off, pointing to idle animation in our self.animations list
        self.current_animation_idx = ANIM_IDLE
        self.current_state = STATE_IDLE
        self.x = x
        self.y = y
        self.velo_x = 0
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.facing_right = True

    def update(self, dt: float):
        self._get_current_anim().update(dt)
        self.x += self.velo_x * dt

    def draw(self, display: pygame.Surface):
        """The anchor point for this player is the bottom center"""
        current_frame, anchor_dx = self._get_current_anim().render(self.width, self.height, self.facing_right)
        pygame.draw.rect(display, (255, 255, 255),  (int(self.x), int(self.y), self.width, self.height))
        display.blit(current_frame, (self.x - anchor_dx, self.y))

    def run_left(self):
        self.current_animation_idx = ANIM_RUNNING
        self._get_current_anim().reset()  # reset the animation to start
        self.current_state = STATE_RUNNING
        self.velo_x = VELO_X * -1
        self.facing_right = False

    def run_right(self):
        self.current_animation_idx = ANIM_RUNNING
        self._get_current_anim().reset()  # reset the animation to start
        self.current_state = STATE_RUNNING
        self.velo_x = VELO_X
        self.facing_right = True

    def idle(self):
        self.current_animation_idx = ANIM_IDLE
        self._get_current_anim().reset()  # reset the animation to start
        self.current_state = STATE_IDLE
        self.velo_x = 0

    def _get_current_anim(self):
        return self.animations[self.current_animation_idx]

    def _load_anims(self) -> List[Animation]:
        """Source: https://www.gameart2d.com/the-boy---free-sprites.html"""
        dist_to_player_feet_in_pixels = 130
        idle_animation = Animation(16, should_loop=True, anchor=dist_to_player_feet_in_pixels)
        for i in range(1, 16):
            idle_file_name = 'Idle (' + str(i) + ').png'
            idle_animation.add_frame('flatboy/' + idle_file_name)

        run_animation = Animation(16, should_loop=True, anchor=dist_to_player_feet_in_pixels)
        for i in range(1, 16):
            run_file_name = 'Run (' + str(i) + ').png'
            run_animation.add_frame('flatboy/' + run_file_name)

        return [idle_animation, run_animation]
