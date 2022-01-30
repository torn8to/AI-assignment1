# takes a map and the current coordinates and returns the frontier for those coordinates.
# frontier is returned as a list of coordinates and a cost, the cost includes turning.
def frontier(map, x, y, orientation):
    i = 0
    children = []
    if x > 1:
        children.append([x-2, y, map[y][x-2] + 3])
        children.append([x-1, y, map[y][x-1]])
    if x == 1:
        children.append([x-1, y, map[y][x-1]])
    if x < len(map[0])-2:
        children.append([x+2, y, map[y][x+2] + 3])
        children.append([x+1, y, map[y][x+1]])
    if x == len(map[0])-2:
        children.append([x+1, y, map[y][x+1]])
    if y > 1:
        children.append([x, y-2, map[y-2][x] + 3])
        children.append([x, y-1, map[y-1][x]])
    if y ==1:
        children.append([x, y-1, map[y-1][x]])
    if y < len(map)-2:
        children.append([x, y+2, map[y+2][x] + 3])
        children.append([x, y+1, map[y+1][x]])
    if y == len(map)-2:
        children.append([x, y+1, map[y+1][x]])
    while i < len(children):
        parent_value = map[y][x]
        child_value = children[i][2]
        if parent_value == "S":
            parent_value = 1
            new_value = child_value
        else:
            new_value = parent_value + child_value
        child_y = children[i][1]
        child_x = children[i][0]
        if orientation == "North":
            if y > child_y:
                children[i][2] = new_value
                children[i].append("North")
                i = i + 1
            if y < child_y:
                children[i][2] = new_value + 2*(math.ceil(parent_value/2))
                children[i].append("South")
                i = i + 1
            if x < child_x:
                children[i][2] = new_value + math.ceil(parent_value / 2)
                children[i].append("East")
                i = i + 1
            if x > child_x:
                children[i][2] = new_value + math.ceil(parent_value / 2)
                children[i].append("West")
                i = i + 1
        if orientation == "South":
            if y < child_y:
                children[i][2] = new_value
                children[i].append("South")
                i = i + 1
            if y > child_y:
                children[i][2] = new_value + 2*(math.ceil(parent_value / 2))
                children[i].append("North")
                i = i + 1
            if x < child_x:
                children[i][2] = new_value + math.ceil(parent_value / 2)
                children[i].append("West")
                i = i + 1
            if x > child_x:
                children[i][2] = new_value + math.ceil(parent_value / 2)
                children[i].append("East")
                i = i + 1
        if orientation == "East":
            if x < child_x:
                children[i][2] = new_value
                children[i].append("East")
                i = i + 1
            if x > child_x:
                children[i][2] = new_value + 2*(math.ceil(parent_value / 2))
                children[i].append("West")
                i = i + 1
            if y < child_y:
                children[i][2] = new_value + math.ceil(parent_value / 2)
                children[i].append("North")
                i = i + 1
            if y > child_y:
                children[i][2] = new_value + math.ceil(parent_value / 2)
                children[i].append("South")
                i = i + 1
        if orientation == "West":
            if x > child_x:
                children[i][2] = new_value
                children[i].append("East")
                i = i + 1
            if x < child_x:
                children[i][2] = new_value + 2*(math.ceil(parent_value / 2))
                children[i].append("West")
                i = i + 1
            if y > child_y:
                children[i][2] = new_value + math.ceil(parent_value / 2)
                children[i].append("North")
                i = i + 1
            if y < child_y:
                children[i][2] = new_value + math.ceil(parent_value / 2)
                children[i].append("South")
                i = i + 1
    return(children)
