from typing import Tuple

import pygame


class Animation:
    def __init__(self, fps: int, should_loop: bool, anchor=None):
        self.frames = []
        self.elapsed_time = 0
        self.fps = fps
        self.should_loop = should_loop
        self.anchor = anchor

    def add_frame(self, frame_path: str):
        frame = pygame.image.load('assets/' + frame_path)
        self.frames.append(frame)

    def update(self, dt):
        """dt is time in miliseconds"""
        self.elapsed_time += dt

    def reset(self):
        self.elapsed_time = 0

    def render(self, width: int, height: int, flip: bool) -> Tuple[pygame.Surface, int]:
        curr_frame = int(self.elapsed_time * self.fps / 1000)
        if self.should_loop:
            curr_frame = curr_frame % len(self.frames)
        elif curr_frame >= len(self.frames):
            curr_frame = len(self.frames) - 1
        return self.scale_image_with_anchor(self.frames[curr_frame], width, height, flip)

    def scale_image_with_anchor(self, current_frame: pygame.Surface, width: int, height: int, flip: bool) -> \
            Tuple[pygame.Surface, int]:
        """
        This function was a doozy. Basically it does three things.
        (1) Scale the image from it's native resolution down to the given width/height WITHOUT distorting aspect ratio
        (2) Flips the image across the X axis
        (3) If the character has an anchor point (like the kid's legs), then flipping the image will "transport"
            the character. "anchor_point_dx" corrects for this offset.

        :returns A tuple. First item is the image. The second item is the distance in the X direction
        the character will be transported.
        """
        frame_w, frame_h = current_frame.get_width(), current_frame.get_height()
        ratio = max(width / frame_w, height / frame_h)
        scaled_w, scaled_h = int(frame_w * ratio), int(frame_h * ratio)
        scaled_frame = pygame.transform.scale(current_frame, (scaled_w, scaled_h))
        anchor_point_dx = 0
        if not flip and self.anchor:
            scaled_anchor = self.anchor / current_frame.get_width() * scaled_w
            scaled_frame = pygame.transform.flip(scaled_frame, True, False)
            anchor_point_dx = scaled_w - scaled_anchor * 2

        return scaled_frame, anchor_point_dx
