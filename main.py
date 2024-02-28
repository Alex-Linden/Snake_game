import pygame
from pygame.locals import *


class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpeg").convert()
        self.x = 100
        self.y = 100

    def draw(self):
        self.surface.fill((58, 13, 79))
        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((500, 500))
        self.surface.fill((58, 13, 79))
        self.snake = Snake(self.surface)
        self.snake.draw()

        # self.block = pygame.image.load("resources/block.jpeg").convert()
        # self.block_x, self.block_y = 100, 100
        # self.surface.blit(self.block, (self.block_x, self.block_y))

        # pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_LEFT:
                        self.block_x -= 10
                        self.draw_block()
                    if event.key == K_RIGHT:
                        self.block_x += 10
                        self.draw_block()
                    if event.key == K_UP:
                        self.block_y -= 10
                        self.draw_block()
                    if event.key == K_DOWN:
                        self.block_y += 10
                        self.draw_block()
                elif event.type == QUIT:
                    running = False


if __name__ == "__main__":
    game = Game()
    game.run()
