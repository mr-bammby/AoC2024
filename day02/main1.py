#!/usr/bin/python3

file = open("input0.txt", "r")
ret = 0

DEC = -1
INC = 1

NORMAL = 0
DAMPENER = 1
DAMPENED = 2


def data_chk(data):
    if (data[1] > data[0]):
        dir = INC
    else:
        dir = DEC
    for i in range(1,len(data)):
        diff = (data[i] - data[i-1]) * dir
        if ((diff <= 0) or (diff > 3)):
            return(i)
    return (0)
    

for line in file:
    if (line[-1] == '\n'):
        line = line[:-1]
    data =  [int(x) for x in line.split(" ")]
    idx = data_chk(data) #check full line
    if (idx == 0):
        ret += 1
        continue
    if (idx == 2): 
        temp = data_chk(data[1:]) #in case of error found between 2. and 3. number also remove fist element example [5,7,6,5,4,3]
        if (temp == 0):
            ret += 1
            continue
    data_cpy = data.copy()
    del data_cpy[idx - 1] #check list with removed first "error element"
    temp = data_chk(data_cpy)
    if (temp == 0):
        ret += 1
        continue
    del data[idx] #check list with removed second "error element"
    temp = data_chk(data)
    if (temp == 0):
        ret += 1
        continue
            

file.close()


print(ret)
    