"""
Attack equipment for battles.
"""
import copy
import pygame as pg
from .. import tools, setup


class Sword(object):
    """
    Sword that appears during regular attacks.
    """
    def __init__(self, player):
        self.player = player
        self.sprite_sheet = setup.GFX['shopsigns']
        self.image_list = self.make_image_list()
        self.index = 0
        self.timer = 0.0

    def make_image_list(self):
        """
        Make the list of two images for animation.
        """
        image_list = [tools.get_image(48, 0, 16, 16, self.sprite_sheet),
                      tools.get_image(0, 0, 22, 16, setup.GFX['sword2'])]
        return image_list

    @property
    def image(self):
        new_image = self.image_list[self.index]
        return pg.transform.scale2x(new_image)

    @property
    def rect(self):
        new_rect = copy.copy(self.player.rect)
        new_rect.bottom += 17
        new_rect.right -= 16
        return new_rect

    def update(self, current_time):
        if (current_time - self.timer) > 60:
            self.timer = current_time
            if self.index == 0:
                self.index += 1
            else:
                self.index -= 1

    def draw(self, surface):
        """
        Draw sprite to surface.
        """
        if self.player.state == 'attack':
            surface.blit(self.image, self.rect)
