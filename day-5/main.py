#!/bin/python3

total = 0
corrected_total = 0

with open("input") as f:
    rules, page_ordering = f.read().split("\n\n")
    rules,page_ordering = rules.split("\n"), page_ordering.split("\n")

def check(item1, item2):
    for rule in rules:
        r = rule.split("|")
        if(int(r[0]) == int(item1) and int(r[1]) == int(item2)):
            return True
    return False

def solve(order):
    order = order.split(",")
    done = False
    while(not done):
        done = True
        for i in range(len(order) - 1):
            if(not check(order[i], order[i+1])):
                s = order[i + 1]
                order[i + 1] = order[i]
                order[i] = s
                done = False
        if(done): break
    return order

for order in page_ordering:
    previous_item = None
    correct = True
    if(order == ""): continue
    for item in order.split(","):
        if(not previous_item): previous_item = item; continue
        if(not check(previous_item,item)): correct = False
        previous_item = item
    if(not correct):
        order = solve(order)
        corrected_total += int(order[int(len(order) / 2)])
        continue

    c = order.split(",")
    total += int(c[int(len(c) / 2)])

print(f"{total=}, {corrected_total=}")
