#!/usr/bin/python3

file = open("input0.txt", "r")

COMMAND_MUL = "mul("
COMM_MUL_LEN = 4
DELIM = ","
COMM_END = ")"

COMMMAND_EN = "do()"
COMM_EN_LEN = 4

COMMMAND_DIS = "don't()"
COMM_DIS_LEN = 7

FIND_COMM = 0
FIRST_NUM = 1
SECOND_NUM = 2

state = FIND_COMM
old_state = FIND_COMM
enable = 1

comm_mul_cnt = 0
comm_en_cnt = 0
comm_dis_cnt = 0

num_str = ""
num1 = 0

ret = 0

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
            if (ch == COMMAND_MUL[comm_mul_cnt]):
                comm_mul_cnt += 1
            elif (ch == COMMAND_MUL[0]):
                comm_mul_cnt = 1
            else:
                comm_mul_cnt = 0
            if (ch == COMMMAND_EN[comm_en_cnt]):
                comm_en_cnt += 1
            elif (ch == COMMMAND_EN[0]):
                comm_en_cnt = 1
            else:
                comm_en_cnt = 0
            if (ch == COMMMAND_DIS[comm_dis_cnt]):
                comm_dis_cnt += 1
            elif (ch == COMMMAND_DIS[0]):
                comm_dis_cnt = 1
            else:
                comm_dis_cnt = 0
            if (comm_mul_cnt == COMM_MUL_LEN):
                comm_mul_cnt = 0
                num_str = ""
                state = FIRST_NUM
            if (comm_en_cnt == COMM_EN_LEN):
                comm_en_cnt = 0
                enable = 1
            if (comm_dis_cnt == COMM_DIS_LEN):
                comm_dis_cnt = 0
                enable = 0

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
                ret += num1 * int(num_str) * enable
                state = FIND_COMM
            else:
                state = FIND_COMM
        case _:
            print("Unkonown state ")



file.close()


print(ret)
    