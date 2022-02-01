import sys
import psutil, os
from datetime import datetime
from map_generation import map_generator,Map
from stokleyAstar import PaFinder#,# heuristic
sys.setrecursionlimit(5000)
process = psutil.Process(os.getpid())


    #tskrd the current memory state of the machine to compare against the ending state

initial_mem = process.memory_info().rss
start = datetime.now()


map = map_generator.generate_random_map(rows=50, cols=50)
map_generator.map_to_file(map)

initial_mem = process.memory_info().rss
start = datetime.now()
# heuristic=heuristic.ZERO
(print(map.map))
finder = PaFinder(map.map)
finder.iterator()

print('memory used: ' + str(round((process.memory_info().rss- initial_mem)/((1024)**2))) + ' mb')
print('time elapsed: ' + str(datetime.now()-start))
