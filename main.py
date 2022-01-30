import sys
import psutil, os
from map_generation import map_generator,Map
from stokleyAstar import PaFinder

process = psutil.Process(os.getpid())

if __name__ =='__main__':
    #tskrd the current memory state of the machine to compare against the ending state
    if len(sys.argv) == 1:
        map = map_generator.generate_random_map(5,5)
        print(map_generator.map_to_string(map.map))

    else:
        file_path = sys.argv[1]
        file = open(file_path)
        map = map_generator.file_to_map(file)
        (print(map.map))
        finder = PaFinder([[4, "G", 4, 6],
                            [2, 9, 9, 6],
                            [1, 4, "S", 3]])
        finder.create_frontier()
        finder.iterator()


    print(process.memory_info().rss)  # in bytes