from Config import *

class Snake:
    def __init__(self, display_surface, start_x=0, start_y=0, start_color=COLORS["Naples Yellow"], player_controlled=True):
        self.rect = pygame.Rect(start_x, start_y, BLOCK_SIZE, BLOCK_SIZE)
        self.player_controlled = player_controlled
        self.color = start_color
        self.direction = 1

        self.display_surface = display_surface
        self.move_delay = 600  # Time in MS before aloud to move again
        self.time_since_moved = time.time()
        self.delta_time = 0

        self.alive = True

        self.can_loop = True

    def update(self):
        self.delta_time = self.time_since_moved - time.time()

        if -self.delta_time >= (self.move_delay / 1000):
            self.time_since_moved = time.time()
            self.move()

    def draw(self):
        pygame.draw.rect(self.display_surface, self.color, self.rect)

    def update_direction(self, key):

        if key == K_w:
            if self.direction != 2:
                self.direction = 0

        if key == K_d:
            if self.direction != 3:
                self.direction = 1

        if key == K_s:
            if self.direction != 0:
                self.direction = 2

        if key == K_a:
            if self.direction != 1:
                self.direction = 3

    def move(self):
        if self.direction == 0:
            self.rect.y -= self.rect.width

        if self.direction == 1:
            self.rect.x += self.rect.width

        if self.direction == 2:
            self.rect.y += self.rect.width

        if self.direction == 3:
            self.rect.x -= self.rect.width

        self.check_collision()

    def check_collision(self):
        def border_checks():
            if self.rect.x >= SNAKE_SURFACE_SIZE:
                if DEBUG_MODE: print("Max X Border")
                return "max_x"
            if self.rect.x < 0:
                if DEBUG_MODE: print("Min X Border")
                return "min_x"

            if self.rect.y >= SNAKE_SURFACE_SIZE:
                if DEBUG_MODE: print("Max Y Border")
                return "max_y"
            if self.rect.y < 0:
                if DEBUG_MODE: print("Min Y Border")
                return "min_y"

        collision = border_checks()

        match collision:
            case "min_x":
                if self.can_loop:
                    self.rect.x = SNAKE_SURFACE_SIZE - self.rect.width
                else:
                    self.die()

            case "max_x":
                if self.can_loop:
                    self.rect.x = 0
                else:
                    self.die()

            case "min_y":
                if self.can_loop:
                    self.rect.y = SNAKE_SURFACE_SIZE - self.rect.height
                else:
                    self.die()

            case "max_y":
                if self.can_loop:
                    self.rect.y = 0
                else:
                    self.die()

    def die(self):
        self.alive = False

