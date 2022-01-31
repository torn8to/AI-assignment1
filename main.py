import sys
import psutil, os
from map_generation import map_generator,Map
from stokleyAstar import PaFinder,heuristic
sys.setrecursionlimit(5000)
process = psutil.Process(os.getpid())

if __name__ =='__main__':
    #tskrd the current memory state of the machine to compare against the ending state

    if len(sys.argv) == 1:
        map = map_generator.generate_random_map(rows=20,cols=20)
        map_generator.map_to_file(map)

    else:
        init_mem = process.memory_info().rss
        file_path = sys.argv[1]
        file = open(file_path)
        map = map_generator.file_to_map(file)
        (print(map.map))
        finder = PaFinder(map.map,heuristic=heuristic.ZERO)
        finder.create_frontier()
        finder.iterator()
        end_mem = process.memory_info().rss
        print((end_mem-init_mem)/(1024**3))

