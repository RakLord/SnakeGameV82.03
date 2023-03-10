import sys
import pygame
from pygame.locals import *
import numpy as np
import time
import random

pygame.font.init()
font = pygame.font.SysFont(None, 24)




DEBUG_MODE = True

SCREEN_SIZE = 900
SNAKE_SURFACE_SIZE = 600
BLOCK_SIZE = SNAKE_SURFACE_SIZE // 15

COLORS = {"Dark Purple" :      (22, 12, 40),
          "Naples Yellow" :    (239, 203, 104),
          "Honeydew" :         (225, 239, 230),
          "Ash Gray" :         (174, 183, 179),
          "Rich Black" :       (0, 4, 17)}

UPGRADE_SIZE = [290, 100]
UPGRADE_Y_PAD = 6

