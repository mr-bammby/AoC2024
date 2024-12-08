#!/usr/bin/python3
import math

file = open("input0.txt", "r")
ret = 0

ant_name = []
ant_lists = []
first_line = True
map_len = 0
map_high = 0
antinodes = set()


for line in file:
    if (line[-1] == '\n'):
        line = line[:-1]
    data = list(line)
    x_cnt = 0
    for char in data:
        if (char != "."):
            if (char in ant_name):
                idx = ant_name.index(char)
                (ant_lists[idx]).append((x_cnt, map_high))
            else:
                ant_name.append(char)
                ant_lists.append([(x_cnt, map_high)])
        x_cnt += 1
    if (first_line):
        map_len = x_cnt
        first_line = False
    map_high += 1
            
file.close()

for ant_list in ant_lists:
    list_len = len(ant_list)
    if (list_len <= 1):
        continue
    for i in range(list_len):
        for j in range(i+1, list_len):
            y_diff = ant_list[i][1] - ant_list[j][1]
            x_diff = ant_list[i][0] - ant_list[j][0]
            if ((ant_list[i][0] + x_diff) >= 0) and ((ant_list[i][1] + y_diff) >= 0) and ((ant_list[i][0] + x_diff) < map_len) and ((ant_list[i][1] + y_diff) < map_high):
                antinodes.add((ant_list[i][0] + x_diff, ant_list[i][1] + y_diff))
            if ((ant_list[j][0] - x_diff) >= 0) and ((ant_list[j][1] - y_diff) >= 0) and ((ant_list[j][0] - x_diff) < map_len) and ((ant_list[j][1] - y_diff) < map_high):
                antinodes.add((ant_list[j][0] - x_diff, ant_list[j][1] - y_diff))

print(len(antinodes))   