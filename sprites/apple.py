import pygame

from sprites.anim import Animation


WIDTH = 32
HEIGHT = 32


class Apple(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.animation = self._load_anim()

    def update(self, dt: float):
        """
        This function is called everytime 1/60th of a second passes.
        We should use this chance to make changes to the apple's position.
        :param dt elapsed in milliseconds
        """
        self.animation.update(dt)
        # TODO(@JB): HUH, THE APPLE ISN'T FALLING.
        # PROBABILY BECAUSE WE DON'T CHANGE THE 'Y' VALUE

    def draw(self, display: pygame.Surface):
        img, offset_x = self.animation.render(WIDTH, HEIGHT, False)
        display.blit(img, (self.x + offset_x, self.y))

    def _load_anim(self) -> Animation:
        apple_anim = Animation(24, should_loop=True)
        for i in range(2, 49):
            apple_file_name = 'apple-rotating-' + str(i) + '.png'
            apple_anim.add_frame('./apple/' + apple_file_name)
        return apple_anim

