from Config import *
from Snake import Snake
from Utilities import *

pygame.init()
pygame.display.set_caption("Snek")

screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

clock = pygame.time.Clock()


snake_surface = pygame.Surface([SNAKE_SURFACE_SIZE, SNAKE_SURFACE_SIZE])
snake = Snake(snake_surface)
while True:
    screen.fill(COLORS["Ash Gray"])
    snake_surface.fill(COLORS["Honeydew"])

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

            snake.update_direction(event.key)

    snake.update()
    snake.draw()

    draw_grid(snake_surface)  # Draws empty grid lines

    screen.blit(snake_surface, (SCREEN_SIZE - SNAKE_SURFACE_SIZE, SCREEN_SIZE - SNAKE_SURFACE_SIZE))
    pygame.display.update()
    clock.tick(60)


