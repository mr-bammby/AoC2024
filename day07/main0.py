#!/usr/bin/python3

file = open("input0.txt", "r")
ret = 0


def rec (arr, arr_len, index, curr_num, result):
    if (index == arr_len):
        return curr_num == result
    elif (curr_num > result):
        return False
    if (rec(arr, arr_len, index + 1, curr_num + arr[index], result)):
        return True
    return rec(arr, arr_len, index + 1, curr_num * arr[index], result)
        


for line in file:
    if (line[-1] == '\n'):
        line = line[:-1]
    result, numbers = line.split(": ")
    numbers =  [int(x) for x in numbers.split(" ")]
    result = int(result)
    if (rec(numbers, len(numbers), 1, numbers[0], result)):
        ret += result
            

file.close()


print(ret)
    