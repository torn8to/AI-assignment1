import sys
import os
from map_generation import map_generator
from robot import Robot
from robot import Heuristic
import time


if __name__ =='__main__':
    total_memory, initial_used_memory, free_memory = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
    if len(sys.argv) == 1:
        map = map_generator.generate_random_map(5,5)
        print(map_generator.map_to_string(map.map))
        robot = Robot(map, Heuristic.SUM, map.starting_pos)
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
    total_memory, used_memory, free_memory = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
    print(used_memory-initial_used_memory)