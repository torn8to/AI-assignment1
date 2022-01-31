import sys
import psutil, os
from datetime import datetime
from map_generation import map_generator,Map
from stokleyAstar import PaFinder,heuristic
sys.setrecursionlimit(5000)
process = psutil.Process(os.getpid())


if __name__ =='__main__':
    #tskrd the current memory state of the machine to compare against the ending state

    initial_mem = process.memory_info().rss
    start = datetime.now()

    if len(sys.argv) == 1:
        map = map_generator.generate_random_map(rows=4000,cols=4000)
        map_generator.map_to_file(map)

    else:
        initial_mem = process.memory_info().rss
        start = datetime.now()

        file_path = sys.argv[1]
        file = open(file_path)
        map = map_generator.file_to_map(file)
        (print(map.map))
        finder = PaFinder(map.map,heuristic=heuristic.zero)
        finder.create_frontier()
        finder.iterator()

    print('memory used: ' + str(round((process.memory_info().rss- initial_mem)/((1024)**2))) + ' mb')
    print('time elapsed: ' + str(datetime.now()-start))
