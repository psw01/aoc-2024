#!/bin/python3

success = 0
def check(line, f=None):
    last_item = None
    increasing = None

    for i, n in enumerate(line.split(" ")):
        if(i == f): continue
        if(not last_item): last_item = n; continue
        dif = int(last_item) - int(n)
        if(abs(dif) > 3 or dif == 0): return False
        if(increasing == None): increasing = True if dif <= 0 else False
        if(increasing and dif > 0): return False 
        if(not increasing and dif < 0): return False 
    
        last_item = n
    return True

with open("input") as f:
    for line in f:
        if(check(line)): success += 1
        else:
            for i in range(len(line.strip())):
                if(check(line, i)):
                    success += 1
                    break

print(f"{success=}")

