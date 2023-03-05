from Config import *


class UpgradeTemplate(object):
    def __init__(self, game_screen):
        self.game_screen = game_screen
        self.size = self.x_size, self.y_size = UPGRADE_SIZE
        self.x = 0
        self.y = 0
        self.surface = pygame.Surface(self.size)  # Parent Container that will be stamped onto the game screen, contain all sub-menus inside of this one

    def draw(self):
        self.surface.fill((255, 255, 255))
        pygame.Surface.blit(self.game_screen, self.surface, (self.x, self.y))


class SnakeSpeedUpgrade(UpgradeTemplate):
    def __init__(self, game_screen):
        super(SnakeSpeedUpgrade, self).__init__(game_screen)
        self.name = "Speed Upgrade"
        self.base_cost = 5
        self.cost = self.base_cost
        self.level = 0

    def update(self):
        self.cost = self.level ** 0.5


class UpgradeManager:
    def __init__(self, game_screen):
        self.game_screen = game_screen

        self.scroll_offset = 0
        self.available_upgrade_list = list()
        self.available_upgrade_list.append(SnakeSpeedUpgrade(game_screen))

    def draw(self):
        for upgrade in self.available_upgrade_list:
            upgrade.draw()

    def update(self):
        for i, upgrade in enumerate(self.available_upgrade_list):
            upgrade.y = i * (upgrade.y_size + UPGRADE_Y_PAD) + self.scroll_offset

        self.draw()


