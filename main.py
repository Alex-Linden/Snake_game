import pygame
import time

if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode((500, 500))
    surface.fill((255, 255, 255))
    pygame.display.flip()

    time.sleep(5)