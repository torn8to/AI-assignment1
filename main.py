import sys


if __name__ =='__main__':
    if len(sys.argv) == 0:
        pass
        #todo: implement random map  generation
    else:
        file_path = sys.argv[1]
        file = open(file_path)
        map = []
        row = file.readline().split()
        while(len(row) != 0):
            map.append(row)
            row = file.readline().split()
        print(type(map))
        #todo: do something with the map object
    print('yeeah')

