XMAS = "XMAS"
XMSA_LEN = 4
ret = 0
first_line = True
line_len = 0
map_len = 2
word_map = []

def check_right(word_map, x, y, cnt):
    global ret

    x += 1
    if (cnt == XMSA_LEN):
        ret += 1
    elif (XMAS[cnt] == word_map[y][x]):
        check_right(word_map, x, y, cnt + 1)
    return

def check_left(word_map, x, y, cnt):
    global ret

    x -= 1
    if (cnt == XMSA_LEN):
        ret += 1
    elif (XMAS[cnt] == word_map[y][x]):
        check_left(word_map, x, y, cnt + 1)
    return

def check_down(word_map, x, y, cnt):
    global ret

    y -= 1
    if (cnt == XMSA_LEN):
        ret += 1
    elif (XMAS[cnt] == word_map[y][x]):
        check_down(word_map, x, y, cnt + 1)
    return

def check_up(word_map, x, y, cnt):
    global ret

    y += 1
    if (cnt == XMSA_LEN):
        ret += 1
    elif (XMAS[cnt] == word_map[y][x]):
        check_up(word_map, x, y, cnt + 1)
    return

def check_rightup(word_map, x, y, cnt):
    global ret

    x += 1
    y -= 1
    if (cnt == XMSA_LEN):
        ret += 1
    elif (XMAS[cnt] == word_map[y][x]):
        check_rightup(word_map, x, y, cnt + 1)
    return

def check_rightdown(word_map, x, y, cnt):
    global ret

    x += 1
    y += 1
    if (cnt == XMSA_LEN):
        ret += 1
    elif (XMAS[cnt] == word_map[y][x]):
        check_rightdown(word_map, x, y, cnt + 1)
    return

def check_leftup(word_map, x, y, cnt):
    global ret

    x -= 1
    y -= 1
    if (cnt == XMSA_LEN):
        ret += 1
    elif (XMAS[cnt] == word_map[y][x]):
        check_leftup(word_map, x, y, cnt + 1)
    return

def check_leftdown(word_map, x, y, cnt):
    global ret

    x -= 1
    y += 1
    if (cnt == XMSA_LEN):
        ret += 1
    elif (XMAS[cnt] == word_map[y][x]):
        check_leftdown(word_map, x, y, cnt + 1)
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
        if (word_map[y][x] == XMAS[0]):
            check_right(word_map, x, y, 1)
            check_left(word_map, x, y, 1)
            check_up(word_map, x, y, 1)
            check_down(word_map, x, y, 1)
            check_rightup(word_map, x, y, 1)
            check_rightdown(word_map, x, y, 1)
            check_leftup(word_map, x, y, 1)
            check_leftdown(word_map, x, y, 1)

print(ret)