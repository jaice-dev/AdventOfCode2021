import math

with open('input.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    lines = [[int(num) for num in line] for line in lines]

print(lines)

low_points = []
visited = [[[False for num in line] for line in lines]]

for i in range(len(lines)):
    for j in range(len(lines[0])):

        left = lines[i][j - 1] if j > 0 else math.inf
        right = lines[i][j + 1] if j < len(lines[0]) - 1 else math.inf
        top = lines[i - 1][j] if i > 0 else math.inf
        bottom = lines[i + 1][j] if i < len(lines) - 1 else math.inf

        location = lines[i][j]

        if location < min(left, right, top, bottom):
            low_points.append([i, j])


def neighbours(y, x):
    neighs = [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
    return [(a, b) for a, b in neighs if 0 <= a < len(lines) and 0 <= b < len(lines[0])]


def get_basin(y, x):
    basin = {(y, x)}
    for a, b in neighbours(y, x):
        if lines[y][x] < lines[a][b] < 9:
            basin |= get_basin(a, b)
    return basin


basin_sizes = sorted([len(get_basin(y, x)) for y, x in low_points])
print(basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])
