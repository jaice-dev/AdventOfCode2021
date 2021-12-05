with open('input.txt') as file:
    lines = file.readlines()
    print(lines)
    lines = [line.rstrip().split(" -> ") for line in lines]
    print(lines)
    lines = [[[int(line[0].split(",")[0]), int(line[0].split(",")[1])],
              [int(line[1].split(",")[0]), int(line[1].split(",")[1])]] for line in lines]

# Initialise map
max_x = 0
max_y = 0

for line in lines:
    for point in line:
        if point[0] > max_x:
            max_x = point[0]
        if point[1] > max_y:
            max_y = point[1]

grid_size = max(max_x, max_y)
grid = []
row = [0] * (grid_size + 1)
for i in range(grid_size + 1):
    grid.append(row.copy())

# Draw points on map
for line in lines:
    if line[0][1] == line[1][1]:
        y = line[0][1]
        # ascending
        if line[0][0] < line[1][0]:
            for i in range(line[0][0], line[1][0] + 1):
                grid[i][y] += 1
        # descending
        else:
            for i in range(line[0][0], line[1][0] - 1, -1):
                grid[i][y] += 1

    if line[0][0] == line[1][0]:
        # vertical
        x = line[0][0]
        # ascending
        if line[0][1] < line[1][1]:
            for i in range(line[0][1], line[1][1] + 1):
                grid[x][i] += 1
        # descending
        else:
            for i in range(line[0][1], line[1][1] - 1, -1):
                grid[x][i] += 1

print(grid)

count = 0
for row in grid:
    for num in row:
        if num > 1:
            count += 1
print(count)

