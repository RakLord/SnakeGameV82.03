from Config import *
from Fruit import *


class FruitManager:
    def __init__(self, snake_surface):
        self.snake_surface = snake_surface
        self.fruit_list = list()
        self.spawn_count = 1
        self.spawn_chance = 50
        self.max_fruits = 2
        self.spawn_active = True

        self.spawn_interval = 2000  # Spawn time in MS
        self.delta_time = 0
        self.time_since_spawned = 0

    def update(self):
        for fruit in reversed(self.fruit_list):
            if not fruit.alive:
                self.fruit_list.remove(fruit)

        if self.spawn_active:
            self.delta_time = self.time_since_spawned - time.time()

            if -self.delta_time >= (self.spawn_interval / 1000):
                self.time_since_spawned = time.time()
                if len(self.fruit_list) < self.max_fruits:
                    self.spawn_fruits()

    def spawn_fruits(self):
        if random.random() * 100 <= self.spawn_chance:
            self.fruit_list.append(Fruit(self.snake_surface, self.fruit_list))

    def draw(self):
        for fruit in self.fruit_list:
            fruit.draw()
