from map_generation import map
from enum import Enum
class direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class A_star():
    def __init__(self,map):
        self.map = map



