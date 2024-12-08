#!/usr/bin/python3

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def change_dir():
    global dir
    
    if (dir < LEFT):
        dir += 1
    else:
        dir = UP
        
def walk():
    global map
    global dir
    global loc_y
    global loc_x
    global done
    cnt = 0
    
    while(1):
        if (map[loc_y][loc_x] == "."):
            cnt += 1
            map[loc_y][loc_x] = "X"
        if (dir == UP):
          next_x = loc_x
          next_y = loc_y - 1
        elif (dir == DOWN):
          next_x = loc_x
          next_y = loc_y + 1
        elif (dir == RIGHT):
          next_x = loc_x + 1
          next_y = loc_y
        elif (dir == LEFT):
          next_x = loc_x - 1
          next_y = loc_y
        else:
          print("Wrong dir")
        if (next_x < 0) or (next_y < 0) or (next_x >= map_len) or (next_y >= map_hig):
            done = True
            return cnt
        if map[next_y][next_x] == "#":
            return cnt
        loc_y = next_y
        loc_x = next_x

file = open("input0.txt", "r")

dir = UP
map = []
done = False
map_len = 0
map_hig = 0
loc_y = 0
loc_x = 0
first_line = True
ret = 0

for line in file:
    if (line[-1] == '\n'):
        line = line[:-1]
    if (first_line):
        first_line = False
        map_len = len(line)
    map_line = list(line)
    if "^" in map_line:
        loc_x = map_line.index("^")
        loc_y = map_hig
        map_line[loc_x] = "."
    map.append(map_line)
    map_hig += 1
file.close()

while (1):
    ret += walk()
    if (done):
        break
    change_dir()

print(ret)
    