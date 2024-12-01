#!/bin/python3

with open("input") as f:
    right_values = []
    left_values = []
    for line in f:
        values = line.split("   ")
        left_values.append(int(values[0].strip()))
        right_values.append(int(values[1].strip()))

    similarity_score = 0
    for i in left_values:
        repeated = 0
        for j in right_values:
            if(i == j): repeated += 1
        similarity_score += i * repeated
    print(f"{similarity_score=}")

    distance_sum = 0
    for _ in range(len(left_values)):
        min_l = min(left_values)
        min_r = min(right_values)

        distance_sum += abs(min_l - min_r)

        left_values.remove(min_l)
        right_values.remove(min_r)
    print(f"{distance_sum=}")
