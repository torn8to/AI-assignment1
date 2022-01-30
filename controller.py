from map_generation import map
from enum import Enum
class direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class heuristic(Enum):
    ZERO = 'zero'
    MIN = 'min'
    MAX = 'max'
    SUM = 'sum'
    better_than_sum = 'bet'
    bet_x_three = 'bx3'




class A_star():
    def __init__(self,map,herustic):
        self.map = map
        self.heuristic = herustic
        self.iteration = 0




    def calculate_heuristic(self, current_pos)->int:
        better_than_sum = 0
        print(current_pos)
        comp = abs(current_pos-self.map.goal)
        if self.heuristic == heuristic.ZERO:
            return 0
        elif self.heuristic == heuristic.MIN:
            return min(comp[0],comp[1])
        elif self.heuristic == heuristic.MAX:
            return max(comp[0],comp[1])
        elif self.heuristic == heuristic.SUM:
            return comp[0] + comp[1]
        elif self.heuristic == heuristic.better_than_sum:
            return better_than_sum #todo:find a heuristic better than sum
        elif self.heuristic  == heuristic.bet_x_three:
            return better_than_sum * 3

    def bouandry_detection(self,coords:tuple)-> bool:
        x = coords[0]
        y = coords[1]
        if y<len(map) or y >= 0 or x<len(map[0]) or x >= 0:
            return True
        return False

    def already_searched(self):

    def find_path(self):
        checked = []