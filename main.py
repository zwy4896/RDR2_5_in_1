# @Author: Bluzy
# @Date  : 2021/02/09 Tue
import pygame
import traceback
import sys

from pygame.constants import QUIT

# init
pygame.init()
pygame.mixer.init()

bg_size = width,height = 480,700
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("catch 5")

def main():
    running = True
    while running:
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