import sys
import psutil, os
from map_generation import map_generator,Map
from stokleyAstar import PaFinder,heuristic
sys.setrecursionlimit(5000)
process = psutil.Process(os.getpid())

if __name__ =='__main__':
    #tskrd the current memory state of the machine to compare against the ending state

    if len(sys.argv) == 1:
        map = map_generator.generate_random_map(rows=12,cols=12)
        map_generator.map_to_file(map)

    else:

        file_path = sys.argv[1]
        file = open(file_path)
        map = map_generator.file_to_map(file)
        (print(map.map))
        finder = PaFinder(map.map,heuristic=heuristic.bet_x_three)
        finder.create_frontier()
        finder.iterator()


    print(process.memory_info().rss)