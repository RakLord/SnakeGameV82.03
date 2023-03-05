from Config import *


def draw_grid(surface):
    for x in range(0, SNAKE_SURFACE_SIZE, BLOCK_SIZE):
        for y in range(0, SNAKE_SURFACE_SIZE, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(surface, COLORS["Rich Black"], rect, 1)
