import random
class map_generator():
    def generate_from_list(map = None, starting_pos = None):
        starting_pos = (None,None)
        goal_pos = (None,None)

        for y in range(len(map)):
            for x in range(len(map[0])):
                if map[y][x] == 'S':
                    starting_pos = (x,y)

                if map[y][x] == 'G':
                    goal_pos = (x,y)

        return {
            'map':map,
            'start':starting_pos,
            'goal': goal_pos
        }

    def generate_random_map(self,cols = 10, rows = 10):
        map = []
        for row in range(rows):
            temp_row = []
            for col in range(cols):
                temp_row.append(str(random.randint(1,9)))
            map.append(temp_row)
        goal = (random.randint(0,cols-1),random.randint(0,rows-1))
        start = (random.randint(0,cols-1),random.randint(0,rows-1))
        while goal == start:
            start = (random.randint(0,cols-1),random.randint(0,rows-1))
        map[goal[1]][goal[0]] = 'G'
        map[start[1]][start[0]] = 'S'
        return {
            'map':map,
            'start':start,
            'goal':goal
        }

    def map_to_string(self,map):
        map_string = ''
        for row in map:
            for val in row[:-1]:
                map_string += val + '\t'
            map_string += row[-1]
            map_string += '\n'
        return map_string[:-1]
