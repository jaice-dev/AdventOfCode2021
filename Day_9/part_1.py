import math

with open('input.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    lines = [[int(num) for num in line] for line in lines]

print(lines)



low_points = []

for i in range(len(lines)):
    for j in range(len(lines[0])):

        left = lines[i][j-1] if j > 0 else math.inf
        right = lines[i][j+1] if j < len(lines[0]) - 1 else math.inf
        top = lines[i-1][j] if i > 0 else math.inf
        bottom = lines[i+1][j] if i < len(lines) - 1 else math.inf

        location = lines[i][j]

        if location < min(left, right, top, bottom):
            low_points.append(location + 1)

print(low_points)
print(sum(low_points))




