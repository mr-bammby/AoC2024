#!/usr/bin/python3

file = open("input0.txt", "r")

COMMAND = "mul("
COMM_LEN = 4
DELIM = ","
COMM_END = ")"

FIND_COMM = 0
FIRST_NUM = 1
SECOND_NUM = 2
DONE = 3

ret = 0
state = FIND_COMM
old_state = FIND_COMM
comm_cnt = 0
num_str = ""
num1 = 0

while (1):
    if (state == FIND_COMM) and (old_state != FIND_COMM):
        ch = ch
    else:
        ch = file.read(1)
    if not ch:
        break
    old_state = state
    match state:
        case 0:
            if (ch == COMMAND[comm_cnt]):
                comm_cnt += 1
            else:
                comm_cnt = 0
            if (comm_cnt == COMM_LEN):
                comm_cnt = 0
                num_str = ""
                state = FIRST_NUM
        case 1:
            if (ch.isnumeric()):
                num_str += ch
            elif ((ch == DELIM) and (num_str != "")):
                num1 = int(num_str)
                num_str = ""
                state = SECOND_NUM
            else:
                state = FIND_COMM
        case 2:
            if (ch.isnumeric()):
                num_str += ch
            elif ((ch == COMM_END) and (num_str != "")):
                ret += num1 * int(num_str)
                state = FIND_COMM
            else:
                state = FIND_COMM
        case _:
            print("Unkonown state ")



file.close()


print(ret)
    