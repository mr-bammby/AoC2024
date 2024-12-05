#!/usr/bin/python3
import math

def find_err_rule(update, rules, rules_len):
    first_num_chk = [False] * rules_len
    second_num_chk = [False] * rules_len
    for num in update:
        rule_cnt = 0
        for rule in rules:
            if (num == rule[0]) and (second_num_chk[rule_cnt] == True):
                return rule_cnt
            elif (num == rule[0]):
                first_num_chk[rule_cnt] = True
            elif ((num == rule[1]) and (first_num_chk[rule_cnt] == False)):
                second_num_chk[rule_cnt] = True
            rule_cnt += 1
    return -1


#returns True for error
def check_update(update, rules, rules_len):
    if (find_err_rule(update, rules, rules_len) == -1):
        return False
    else:
        return True

def fix_update(update:list, rules, rules_len):
    while(1):
        err_idx = find_err_rule(update, rules, rules_len)
        if (err_idx == -1):
            return update
        err_rule = rules[err_idx]
        update[update.index(err_rule[0])] = err_rule[1]
        update[update.index(err_rule[1])] = err_rule[0]

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
    err = check_update(update, rules, rules_len)
    if (err):
        fixed_update = fix_update(update, rules, rules_len)
        ret += fixed_update[update_half]


print(ret)
    