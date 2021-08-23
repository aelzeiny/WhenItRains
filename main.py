from game_world import GameWorld

import pygame
import sys

from sprites.apple import Apple
from sprites.player import Player, PLAYER_HEIGHT

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FPS = 60


def init_game() -> GameWorld:
    """This creates our game world"""
    game_world = GameWorld()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT - PLAYER_HEIGHT)
    game_world.add_player(player)

    apple = Apple(SCREEN_WIDTH / 2, 0)
    game_world.add_falling_sprite(apple)

    return game_world


def update(game_world: GameWorld, dt: float):
    """
    Update game. Called once per frame.
    dt is the amount of time passed since last frame.
    If you want to have constant apparent movement no matter your framerate,
    what you can do is something like

    x += v * dt

    and this will scale your velocity based on time. Extend as necessary."""

    # Go through events that are passed to the script by the window.
    for event in pygame.event.get():
        # We need to handle these events. Initially the only one you'll want to care
        # about is the QUIT event, because if you don't handle it, your game will crash
        # whenever someone tries to exit.
        if event.type == pygame.QUIT:
            pygame.quit()  # Opposite of pygame.init
            sys.exit()  # Not including this line crashes the script on Windows. Possibly
            # on other operating systems too, but I don't know for sure.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                game_world.player.idle()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game_world.player.run_left()
            elif event.key == pygame.K_RIGHT:
                game_world.player.run_right()

    # finally we update the gameworld
    game_world.update(dt)

    # Also, let's keep the player in-bounds
    if game_world.player.x < 0:
        game_world.player.x = 0
    if game_world.player.x + game_world.player.width > SCREEN_WIDTH:
        game_world.player.x = SCREEN_WIDTH - game_world.player.width


def draw(game_world: GameWorld, screen):
    """
    Draw things to the window. Called once per frame.
    """
    screen.fill((0, 0, 0))  # Fill the screen with black.
    # Here we draw the gameworld
    game_world.draw(screen)
    # show everything we drew to the player
    pygame.display.flip()


def when_it_rains():
    # Initialise PyGame.
    pygame.init()
    game_world = init_game()

    # Set up the clock. This will tick every frame and thus maintain a relatively constant framerate. Hopefully.
    fps_clock = pygame.time.Clock()

    # Set up the window.
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # screen is the surface representing the window.
    # PyGame surfaces can be thought of as screen sections that you can draw onto.
    # You can also draw surfaces onto other surfaces, rotate surfaces, and transform surfaces.

    # Main game loop.
    dt = 1 / FPS  # dt is the time since last frame.
    while True:  # Loop forever!
        update(game_world, dt)  # You can update/draw here, I've just moved the code for neatness.
        draw(game_world, screen)

        dt = fps_clock.tick(FPS)


if __name__ == "__main__":
    # this line of code only runs if we run 'python main.py'.
    # If we start the program from elsewhere, it does not run.
    when_it_rains()
