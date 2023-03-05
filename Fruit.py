import pygame.sprite

from Config import *


class Fruit:
    def __init__(self, display_surface, fruit_list, start_x=None, start_y=None):
        if not start_x or not start_y:
            start_x = (random.randint(1, SNAKE_SURFACE_SIZE // BLOCK_SIZE)-1) * BLOCK_SIZE
            start_y = (random.randint(1, SNAKE_SURFACE_SIZE // BLOCK_SIZE)-1) * BLOCK_SIZE

        self.display_surface = display_surface
        self.value = 1
        self.color = (220, 20, 29)
        self.rect = pygame.Rect(start_x, start_y, BLOCK_SIZE, BLOCK_SIZE)

        self.alive = True
        for fruit in fruit_list:
            if fruit.rect.x == self.rect.x and fruit.rect.y == self.rect.y:
                self.alive = False
                if DEBUG_MODE: print(f"Killed: {self} | At {self.rect.x // BLOCK_SIZE}, {self.rect.y // BLOCK_SIZE}")



        # check_list = [fruit.rect for fruit in fruit_list if fruit != self]
        # collision_with = self.rect.collidelist(check_list)
        # if collision_with == -1:  # -1 = no collision
        #     self.alive = True
        #
        # else:
        #     self.alive = False
        #     if DEBUG_MODE: print(f"Killed: {self} | At {self.rect.x // BLOCK_SIZE}, {self.rect.y // BLOCK_SIZE}")

    def draw(self):
        pygame.draw.rect(self.display_surface, self.color, self.rect)

