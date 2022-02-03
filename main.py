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
     if input.lower() == '1':
         return heuristic.ZERO
     elif input.lower() == '2':
         return heuristic.MIN
     elif input.lower() == '3':
         return heuristic.MAX
     elif input.lower() == '4':
         return heuristic.SUM
     elif input.lower() == '5':
         return heuristic.better_than_sum
     elif input.lower() == '6':
         return heuristic.bet_x_three
     return heuristic.ZERO

if len(sys.argv) > 1:
    file_path = sys.argv[1]
    file = open(file_path)
    map = map_generator.file_to_map(file)
    heur = determine_heuristic(sys.argv[2])


else:
    map = map_generator.generate_random_map(rows=200, cols=200)
    map_generator.map_to_file(map)
    heur = heuristic.ZERO


initial_mem = process.memory_info().rss
start = datetime.now()

finder = PaFinder(map.map, heuristic=heur)
finder.iterator()

print('memory used: ' + str(round((process.memory_info().rss- initial_mem)/((1024)**2))) + ' mb')
print('time elapsed: ' + str(datetime.now()-start))
