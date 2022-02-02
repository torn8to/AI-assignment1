import sys
import psutil, os
from datetime import datetime
from map_generation import map_generator,Map
from stokleyAstar import PaFinder, heuristic
sys.setrecursionlimit(5000)
process = psutil.Process(os.getpid())

if len(sys.argv) == 1:
    map = map_generator.generate_random_map(rows=565, cols=565)
    initial_mem = process.memory_info().rss
    start = datetime.now()
    map_generator.map_to_file(map)

def determine_heuristic(input):
     if input.lower() == 'zero':
         return heuristic.ZERO
     elif input.lower() == 'min':
         return heuristic.min
     elif input.lower() == 'max':
         return heuristic.MAX
     elif input.lower() == 'sum':
         return heuristic.SUM
     elif input.lower() == 'better':
         return heuristic.better_than_sum
     elif input.lower() == 'betterx3':
         return heuristic.bet_x_three
     return heuristic.ZERO

initial_mem = process.memory_info().rss
start = datetime.now()
if len(len(sys.argv) == 2):
    map = map_generator.file_to_map(sys.argv[1])
    heur = determine_heuristic(sys.argv[2])

else:
    map = map_generator.generate_random_map(rows=200, cols=200)
    map_generator.map_to_file(map)
    heur = heuristic.ZERO

print('memory used: ' + str(round((process.memory_info().rss- initial_mem)/((1024)**2))) + ' mb')
print('time elapsed: ' + str(datetime.now()-start))

start = datetime.now()

finder = PaFinder(map.map, heuristic=heur)
finder.iterator()

print('memory used: ' + str(round((process.memory_info().rss- initial_mem)/((1024)**2))) + ' mb')
print('time elapsed: ' + str(datetime.now()-start))
