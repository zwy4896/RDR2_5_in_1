# @Author: Bluzy
# @Date  : 2021/02/09 Tue

import pygame
import traceback
import sys
import random
import Dominoes
import settings
import game

from pygame.constants import QUIT
from pygame.locals import *

# init
pygame.init()
pygame.mixer.init()

bg_size = width,height = 480,640
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("RDR_5")

def __init__():
    c = Dominoes.Dominoes(screen, (100, 100, 45, 100))
    c.draw()
def main():
    running = True
    while running:
        __init__()
        # Event listener
        for event in pygame.event.get():
            # Quit game
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()