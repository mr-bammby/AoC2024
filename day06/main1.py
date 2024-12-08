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

def make_step():
    global map
    global dir
    global loc_y
    global loc_x
    global done
    
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
        return 1
    if map[next_y][next_x] == "#":
        return 1
    loc_y = next_y
    loc_x = next_x
    return (0)

def walk():
    global map
    global dir
    global loc_y
    global loc_x
    global done
    
    run = 1
    cnt = 0
    while(run):
        if make_step() == 1:
            run = 0
        else:
            cnt += 1
    return (cnt)

def check_loop():
    global map
    global dir
    global loc_y
    global loc_x
    global done
    global new_stones
    global begin_x
    global begin_y
    
    start_x = loc_x
    start_y = loc_y
    start_dir = dir
    ret = 0
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
        return 900000
    if (next_x < 0) or (next_y < 0) or (next_x >= map_len) or (next_y >= map_hig):
        return 0
    if (map[next_y][next_x] == "#"):
        return 0
    if (next_x == begin_x) and (next_y == begin_y):
        return 0
    map[next_y][next_x] = "#"
    coner_set = set()
    while(1):
        coner_set.add((loc_x, loc_y, dir))
        change_dir()
        walk()
        if done:
            break
        if (loc_x, loc_y, dir) in coner_set:
            ret = 1
            if len(coner_set) > 2:
                new_stones.add((next_x, next_y))
            break
    loc_x = start_x
    loc_y = start_y
    dir = start_dir
    map[next_y][next_x] = "."
    done = False
    return ret
        

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
new_stones = set()

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
cnt = 0
begin_x = loc_x
begin_y = loc_y
while (1):
    hit = 0
    while (hit == 0):
        ret += check_loop()
        hit = make_step()
        if (done):
            break
        cnt += 1
        print (cnt)
    if (done):
        break
    change_dir()

print(ret)
print(len(new_stones))