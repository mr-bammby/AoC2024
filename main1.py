MAS = "MAS"
CHK_LEN = 4
ret = 0
first_line = True
line_len = 0
map_len = 2
word_map = []


def get_rightup(word_map, x, y):
    x += 1
    y -= 1
    return word_map[y][x]

def get_rightdown(word_map, x, y):
    x += 1
    y += 1
    return word_map[y][x]

def get_leftup(word_map, x, y):
    x -= 1
    y -= 1
    return word_map[y][x]

def get_leftdown(word_map, x, y):
    x -= 1
    y += 1
    return word_map[y][x]

def check_x(word_map, x, y):
    global ret
    
    m_cnt = 0
    s_cnt = 0
    if (get_rightup(word_map, x, y) == "M"):
        m_cnt += 1
    elif (get_rightup(word_map, x, y) == "S"):
        s_cnt += 1
    else:
        return
    if (get_rightdown(word_map, x, y) == "M"):
        m_cnt += 1
    elif (get_rightdown(word_map, x, y) == "S"):
        s_cnt += 1
    else:
        return
    if (get_leftup(word_map, x, y) == "M"):
        m_cnt += 1
    elif (get_leftup(word_map, x, y) == "S"):
        s_cnt += 1
    else:
        return
    if (get_leftdown(word_map, x, y) == "M"):
        m_cnt += 1
    elif (get_leftdown(word_map, x, y) == "S"):
        s_cnt += 1
    else:
        return
    if (get_leftdown(word_map, x, y) == get_rightup(word_map, x, y)):
        return
    if ((m_cnt == 2) and (s_cnt == 2)):
        ret += 1
    return

f = open("input0.txt", "r")

for line in f:
    split_line = []
    split_line.append("0")
    if (line[-1] == "\n"):
        line = line[:-1]
    line_len = len(line) + 2
    split_line += list(line)
    split_line.append("0")
    if first_line:
        first_line = False
        word_map.append(["0"] * line_len)
    word_map.append(split_line)
    map_len += 1

word_map.append(["0"] * line_len)

f.close()

for y in range(1, map_len - 1):
    for x in range(1, line_len - 1):
        if (word_map[y][x] == "A"):
            check_x(word_map, x, y)

print(ret)