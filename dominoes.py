# @Author: Bluzy
# @Date  : 2020/02/09 Tue
# @Func  : Dominoes class

import pygame

class Dominoes(pygame.sprite.Sprite):
    def __init__(self, surface, rect) -> None:
        super(Dominoes, self).__init__()
        self.surface = surface
        self.rect = pygame.Rect(rect)

    def rot(self):
        # 旋转骨牌方向
        pass

    def reset(self):
        # 重置骨牌方向
        pass

    def draw(self):
        pygame.draw.rect(self.surface, (255, 255, 255), self.rect, 0)