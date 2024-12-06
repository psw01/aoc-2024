import re

data = []
xmas_found = 0
mas_found = 0

with open("./simple_input") as f:
    for line in f:
        if(line.strip() == ""): continue
        data.append([*line.strip()])

def check(t, patterns=[r"(XMAS)", r"(SAMX)"]):
    out = 0
    for pattern in patterns:
        out += len(re.findall(pattern, t))
    return out

# left to right check
for row in data:
    l = "".join(row)
    xmas_found += check(l)

# up and down check
for i in range(len(data[0])):
    l = ""
    for j in range(len(data)):
        l += data[j][i]
    xmas_found += check(l)


# credit: flamedwolf
# diagonal check
for i in range(len(data[0]) - 3):
    for j in range(len(data) - 3):
        w1 = data[i][j + 3] + data[i + 1][j + 2] + data[i + 2][j + 1] + data[i + 3][j]
        w2 = data[i][j] + data[i+1][j+1] + data[i+2][j+2] + data[i+3][j+3]
        xmas_found += check(w1) + check(w2) 


p = [r"(MAS)|(SAM)"]
for h in range(1, len(data)-1):
    for w in range(1, len(data[0])-1):
        if(data[h][w] != "A"): continue
        w1 = data[h - 1 ][w - 1] + data[h][w] + data[h + 1][w + 1]
        w2 = data[h + 1][w - 1] + data[h][w] + data[h - 1][w + 1] 
        if(check(w1, p) + check(w2, p) == 2): mas_found += 1

print(f"{xmas_found=} {mas_found=}")    
