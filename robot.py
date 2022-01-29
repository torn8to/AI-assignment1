from map_generation import Map
from enum import Enum
from enum import IntEnum

class direction(IntEnum):
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


class Robot():
    def __init__(self,map,heuristic,position,direction=direction.NORTH):
        self.map = map
        self.heuristic = heuristic
        self.position = position
        self.direction = direction

    def calculate_heuristic(self,position)->int:
        better_than_sum = 0
        comp = (abs(position[0]-self.map.goal[0]),abs(position[1]-self.map.goal[1]))
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

    # def neighbor_travel_cost(self,neighbor):
    #     cost = self.map.get_terrain(neighbor)

    def get_num_turns(self,dir):
        if(self.direction == direction.NORTH):
            calc_turns = [0,1,2,1]
            return calc_turns[dir]
        if(self.direction == direction.NORTH):
            calc_turns = [1,0,1,2]
            return calc_turns[dir]
        if(self.direction == direction.NORTH):
            calc_turns = [2,1,0,1]
            return calc_turns[dir]
        if(self.direction == direction.NORTH):
            calc_turns = [1,2,1,0]
            return calc_turns[dir]

    def get_neighbors(self):
        neighbors = []
        costs = []
        x = self.position[0]
        y = self.position[1]
        map_x = self.map.max_x
        map_y = self.map.max_y
        # check left
        if(x > 0):
            neighbor = (x-1,y)
            neighbors.append(neighbor)
            terrain = self.map.get_terrain(neighbor)
            cost = self.calculate_heuristic(neighbor) + self.get_num_turns(direction.WEST)*round(0.5 * terrain)+terrain
            costs.append(cost)
        # check above
        if(y > 0):
            neighbor = (x,y-1)
            neighbors.append(neighbor)
            terrain = self.map.get_terrain(neighbor)
            cost = self.calculate_heuristic(neighbor) + self.get_num_turns(direction.NORTH)*round(0.5 * terrain)+terrain
            costs.append(cost)
        # chck right
        if(x < map_x):
            neighbor = (x+1,y)
            neighbors.append(neighbor)
            terrain = self.map.get_terrain(neighbor)
            cost = self.calculate_heuristic(neighbor) + self.get_num_turns(direction.EAST)*round(0.5 * terrain)+terrain
            costs.append(cost)
        # check below
        if(y < map_y):
            neighbor = (x,y+1)
            neighbors.append(neighbor)
            terrain = self.map.get_terrain(neighbor)
            cost = self.calculate_heuristic(neighbor) + self.get_num_turns(direction.SOUTH)*round(0.5 * terrain)+terrain
            costs.append(cost)
        return (neighbors,costs)


    def check_neighbors(self):
        neighbor_info = self.get_neighbors()
        neighbors = neighbor_info[0]
        costs = neighbor_info[1]
        min_cost = costs[0]
        best_neighbor = neighbors[0]
        for i in range(len(neighbors)):
            print(neighbors[i])
            print(costs[i])
            if(costs[i] < min_cost):
                min_cost = costs[i]
                best_neighbor = neighbors[i]
        print("best neighbor is at ")
        print(best_neighbor)
        print("with a value of")
        print(min_cost)
        return best_neighbor
