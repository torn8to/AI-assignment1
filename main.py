import sys
from map_generation import map_generator


if __name__ =='__main__':
    if len(sys.argv) == 0:
        pass
        #todo: implement random map  generation
    else:
        file_path = sys.argv[1]
        file = open(file_path)
        print(map_generator.file_to_map(file))
        #todo: do something with the map object
    print('yeeah')

