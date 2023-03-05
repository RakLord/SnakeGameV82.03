from Config import *
from Snake import Snake
from Utilities import *
from Fruit import Fruit
from Fruit_Manager import FruitManager
from Upgrades import UpgradeManager

pygame.init()
pygame.display.set_caption("Snek")

screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

clock = pygame.time.Clock()


snake_surface = pygame.Surface([SNAKE_SURFACE_SIZE, SNAKE_SURFACE_SIZE])
snake = Snake(snake_surface)

fruit_manager = FruitManager(snake_surface)
upgrade_manager = UpgradeManager(screen)

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
            if event.key == K_q:
                print(len(fruit_manager.fruit_list), fruit_manager.fruit_list)
                for fruit in fruit_manager.fruit_list:
                    print(f"X: {fruit.rect.x / BLOCK_SIZE} | Y: {fruit.rect.y / BLOCK_SIZE} | Status: {fruit.alive}")
                print(f"Snake:  [X: {snake.rect.x / BLOCK_SIZE} | Y: {snake.rect.y / BLOCK_SIZE}]")

                print(upgrade_manager.available_upgrade_list)

                print("Debugged")

            snake.update_direction(event.key)

    fruit_manager.update()
    snake.update(fruit_manager.fruit_list)
    upgrade_manager.update()

    fruit_manager.draw()
    snake.draw()

    # print(len(fruit_list))




    draw_grid(snake_surface)  # Draws empty grid lines

    screen.blit(snake_surface, (SCREEN_SIZE - SNAKE_SURFACE_SIZE, SCREEN_SIZE - SNAKE_SURFACE_SIZE))
    pygame.display.update()
    clock.tick(60)


