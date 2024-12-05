#!/usr/bin/python3
import math


file = open("input0.txt", "r")
rules = []
updates = []
ret = 0
rules_len = 0

for line in file:
    if line == "\n":
        break
    if (line[-1] == '\n'):
        line = line[:-1]
    rule = tuple(int(item) for item in line.split("|"))
    rules.append(rule)

for line in file:
    if (line[-1] == '\n'):
        line = line[:-1]
    update = list(int(item) for item in line.split(","))
    updates.append(update)

file.close()

rules_len = len(rules)


for update in updates:
    update_half = math.floor(len(update) / 2)
    half_num = -1
    first_num_chk = [False] * rules_len
    second_num_chk = [False] * rules_len
    err = False
    num_cnt = 0
    for num in update:
        rule_cnt = 0
        for rule in rules:
            if (num == rule[0]) and (second_num_chk[rule_cnt] == True):
                err = True
                break
            elif (num == rule[0]):
                first_num_chk[rule_cnt] = True
            elif ((num == rule[1]) and (first_num_chk[rule_cnt] == False)):
                second_num_chk[rule_cnt] = True
            rule_cnt += 1
        if (err):
            break
        if (num_cnt == update_half):
            half_num = num
        num_cnt += 1
    if (not err):
        ret += half_num


print(ret)
    