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
    # horizontal
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

    # vertical
    elif line[0][0] == line[1][0]:
        x = line[0][0]
        # ascending
        if line[0][1] < line[1][1]:
            for i in range(line[0][1], line[1][1] + 1):
                grid[x][i] += 1
        # descending
        else:
            for i in range(line[0][1], line[1][1] - 1, -1):
                grid[x][i] += 1

    # diagonal
    else:
        start_x = line[0][0]
        end_x = line[1][0]
        start_y = line[0][1]
        end_y = line[1][1]

        x_dir = 1 if start_x - end_x < 0 else -1
        y_dir = 1 if start_y - end_y < 0 else -1

        while True:
            grid[start_x][start_y] += 1

            if start_x == end_x:
                break

            start_x += x_dir * 1
            start_y += y_dir * 1

print(grid)

count = 0
for row in grid:
    for num in row:
        if num > 1:
            count += 1
print(count)

