import sys
from map_generation import map_generator


if __name__ =='__main__':
    if len(sys.argv) == 0:
        map = map_generator.generate_random_map()
        #todo: implement random map  generation
    else:
        file_path = sys.argv[1]
        file = open(file_path)
        map = map_generator.file_to_map(file)
        #todo: do something with the map object

