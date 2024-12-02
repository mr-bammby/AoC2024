#!/usr/bin/python3

file = open("input0.txt", "r")
ret = 0

DEC = -1
INC = 1


for line in file:
    if (line[-1] == '\n'):
        line = line[:-1]
    data =  [int(x) for x in line.split(" ")]
    num = data[0]
    if (data[1] > data[0]):
        dir = INC
    else:
        dir = DEC
    good_data = 1
    for i in range(1,len(data)):
        diff = (data[i] - data[i-1]) * dir
        if ((diff <= 0) or (diff > 3)):
            good_data = 0
            break
    ret += good_data
            

file.close()


print(ret)
    