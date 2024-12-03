#!/bin/python3

import re

pattern = r"(?<=mul\()(\d+,\d+)(?=\))|(don't\(\))|(do\(\))"
total = 0
enabled = True

with open("input") as f:
    matches = re.findall(pattern, f.read())
    for match in matches:
        if(match[1]): enabled = False; continue
        if(match[2]): enabled = True; continue
        if(enabled):
            total += int(match[0].split(",")[0]) * int(match[0].split(",")[1])

print(total)
