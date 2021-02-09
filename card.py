# @Author: Bluzy
# @Date  : 2020/02/09 Tue
# @Func  : Card class

import pygame

class Card(pygame.sprite.Sprite):
    def __init__(self, direction) -> None:
        pygame.sprite.Sprite.__init__(self)

    def rot(self):
        pass

    def reset(self):
        pass