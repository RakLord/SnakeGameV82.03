from Config import *


class UpgradeTemplate(object):
    def __init__(self, game_screen, level=1, **kwargs):
        self.game_screen = game_screen
        self.size = self.x_size, self.y_size = UPGRADE_SIZE
        self.x = 0
        self.y = 0
        self.surface = pygame.Surface(self.size)  # Parent Container that will be stamped
                                                  # onto the game screen, contain all sub-menus inside of this one

        self.__dict__.update(kwargs)

        self.level = level
        self.cost = round(self.cost_function())

        if "output_function" in self.__dict__:
             print("Output function found")

        if DEBUG_MODE: print(self.__dict__)

    def draw(self):
        self.surface.fill(COLORS["Dark Purple"])
        self.surface.blit(font.render(self.name, True, COLORS["Ash Gray"]), (5, 5))
        self.surface.blit(font.render("$: " + str(self.cost), True, COLORS["Ash Gray"]), (5, 20))
        self.surface.blit(font.render("Lvl: " + str(round(self.level)), True, COLORS["Ash Gray"]), (5, 35))
        self.surface.blit(font.render(self.name, True, COLORS["Ash Gray"]), (5, 50))
        pygame.Surface.blit(self.game_screen, self.surface, (self.x, self.y))


""" To create a new upgrade copy this class below and modify the the cost function. 
When an upgrade level reference is required just directly reference the upgrades level value and use that. If 
required possible to add an output function to allow for more potential."""


class SnakeSpeedUpgrade(UpgradeTemplate):
    def __init__(self, game_screen):
        super(SnakeSpeedUpgrade, self).__init__(game_screen,
                                                name="Speed Upgrade",
                                                base_cost=5,
                                                cost_function=self.cost_function,
                                                #  output_function=self.output_function)
                                                )

    def cost_function(self):
        return self.level ** 0.5
    #
    # def output_function(self):
    #     return self.level * 1.43


class UpgradeManager:
    def __init__(self, game_screen):
        self.game_screen = game_screen

        self.scroll_offset = 0
        self.available_upgrade_list = list()
        self.available_upgrade_list.append(SnakeSpeedUpgrade(game_screen))
        self.available_upgrade_list.append(SnakeSpeedUpgrade(game_screen))
        self.available_upgrade_list.append(SnakeSpeedUpgrade(game_screen))

    def draw(self):
        for upgrade in self.available_upgrade_list:
            upgrade.draw()

    def update(self):
        for i, upgrade in enumerate(self.available_upgrade_list):
            upgrade.y = i * (upgrade.y_size + UPGRADE_Y_PAD) + self.scroll_offset

        self.draw()


