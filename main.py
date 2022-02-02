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

else:
    initial_mem = process.memory_info().rss
    start = datetime.now()

    file_path = sys.argv[1]
    chosen_h = sys.arv[2]
    cur_h = heuristic.ZERO
    if chosen_h == 2:
        cur_h = heuristic.MIN
    elif chosen_h == 3:
        cur_h = heuristic.MAX
    elif chosen_h == 4:
        cur_h = heuristic.SUM
    elif chosen_h == 5:
        cur_h = heuristic.better_than_sum
    elif chosen_h == 6:
        cur_h = heuristic.bet_x_three

    file = open(file_path)
    map = map_generator.file_to_map(file)

    initial_mem = process.memory_info().rss
    start = datetime.now()

    finder = PaFinder(map.map,cur_h)
    finder.iterator()

    print('memory used: ' + str(round((process.memory_info().rss- initial_mem)/((1024)**2))) + ' mb')
    print('time elapsed: ' + str(datetime.now()-start))
