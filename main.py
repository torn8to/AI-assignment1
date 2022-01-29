import sys
from map_generation import map_generator
from robot import Robot
from robot import heuristic
import time


if __name__ =='__main__':
    if len(sys.argv) == 1:
        map = map_generator.generate_random_map(5,5)
        print(map_generator.map_to_string(map.map))
        robot = Robot(map,heuristic.SUM,map.starting_pos)
        # print(robot.calculate_heuristic())
        robot.check_neighbors()
        # start_time = time.time()
        # while(time.time() - start_time < 4)

        #todo: implement random map  generation
    else:
        file_path = sys.argv[1]
        file = open(file_path)
        map = map_generator.file_to_map(file)
        #todo: do something with the map object
