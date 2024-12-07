#!/bin/python3

with open("input") as f:
    map = []
    for row in f:
        map.append(list(row.strip()))

def check(y, x):
    global di_i, finish, loops
    if(x < 0 or y < 0):
        finish = True
        return False
    if(x >= len(map[0]) or y >= len(map)):
        finish = True
        return False
    if(map[y][x] == "#" or map[y][x] == "O"):
        if(stage == 1 and not store(g_y, g_x, di_i)):
            loops += 1
            finish=  True
        di_i += 1
        return False
    return True

def move(direction):
    global g_y, g_x
    match direction:
        case "UP":
            if (check(g_y - 1, g_x)):
                map[g_y][g_x] = "X"
                g_y-=1
        case "DOWN":
            if (check(g_y + 1, g_x)):
                map[g_y][g_x] = "X"
                g_y+=1
        case "LEFT":
            if (check(g_y, g_x - 1)):
                map[g_y][g_x] = "X"
                g_x -= 1
        case "RIGHT":
            if (check(g_y, g_x + 1)):
                map[g_y][g_x] = "X"
                g_x += 1
    map[g_y][g_x] = "^"

def store(y,x,f):
    global history
    p = f"{x}_{y}_{f}"
    if(p in history):
        history[p] += 1
    else:
        history[p] = 0
    if(history[p] > 1):
        return False
    return True

for l in range(len(map)):
    for i in range(len(map[0])):
        if(map[l][i] == "^"):
            g_y, g_x = l, i
            break

finish = False
directions = ["UP", "RIGHT", "DOWN", "LEFT"]
di_i, stage, loops, steps = 0, 0, 0, 0
start_pos_y, start_pos_x = g_y, g_x
history = {}

while(not finish):
    if(di_i > 3): di_i = 0
    move(directions[di_i])

for m in map:
    for i in m:
        if(i == "X"): steps+=1
steps+=1

stage = 1
for h in range(len(map)):
    for w in range(len(map[0])):
        print(h, w, end="\r")
        first, finish = True, False
        g_y, g_x = start_pos_y, start_pos_x
        di_i = 0
        history = {}
        checkpoint_y, checkpoint_x = h, w
        if(map[h][w] in ["#"]): continue
        map[h][w] = "O"
        while(True):
            if(finish): 
                map[g_y][g_x] = "X"
                break
            if(di_i > 3): di_i = 0
            move(directions[di_i])
        map[h][w] = "."

print(f"\n{steps=} {loops=}")
