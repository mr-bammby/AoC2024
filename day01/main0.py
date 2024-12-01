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
list_left.sort()
list_right.sort()

ret = 0
for num1, num2 in zip(list_left, list_right):
    ret += abs(num1 - num2)

print(ret)
    