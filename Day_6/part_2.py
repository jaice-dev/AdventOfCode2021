from collections import deque

with open('input.txt') as file:
    lines = file.readlines()
    lines = [int(num) for line in lines for num in line.split(",")]

print(lines)

def solve(days):
    counts = deque([0]*9)
    for count in lines:
       counts[count] += 1
    for _ in range(days):
        counts.rotate(-1)
        counts[6] += counts[8]
    return sum(counts)

print(solve(256))



