#!/usr/bin/python3

file = open("input0.txt", "r")
list_left = []
list_right = []


for line in file:
    num1, num2 = line.split("   ")
    if (num2[-1] == '\n'):
        num2 = num2[:-1]
    list_left.append(int(num1))
    list_right.append(int(num2))

file.close()
list_right.sort()
ret = 0
for num in list_left:
    cnt = 0
    if num in list_right:
        idx = list_right.index(num)
        cnt = idx
        while (list_right[idx] == num):
            idx += 1
        cnt = idx - cnt
        ret += cnt * num

print(ret)
