from Config import *


class UpgradeTemplate(object):
    def __init__(self, game_screen):
        self.game_screen = game_screen
        self.size = self.x_size, self.y_size = UPGRADE_SIZE
        self.surface = pygame.Surface(self.size)  # Parent Container that will be stamped onto the game screen, contain all sub-menus inside of this one

    def draw(self):
        self.surface.fill((255, 255, 255))
        pygame.Surface.blit(self.game_screen, self.surface, (0, 0))


class SnakeSpeedUpgrade(UpgradeTemplate):
    def __init__(self, game_screen):
        super(SnakeSpeedUpgrade, self).__init__(game_screen)


class UpgradeManager:
    def __init__(self, game_screen):
        self.game_screen = game_screen

        self.available_upgrade_list = list()
        self.available_upgrade_list.append(SnakeSpeedUpgrade(game_screen))

    def draw(self):
        for upgrade in self.available_upgrade_list:
            upgrade.draw()




