
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
        #todo: you 
    def generate_random_map(self,dimension = 15):
        pass

