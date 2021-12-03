with open('depths.txt') as file:
    lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]

count = 0
for i in range(1, len(lines)):
    if lines[i] > lines[i-1]:
        count += 1
print(count)

window_count = 0
for i in range(3, len(lines)):
    sum_prev_window = lines[i-3] + lines[i-2] + lines[i-1]
    sum_current_window = lines[i-2] + lines[i-1] + lines[i]
    if sum_current_window > sum_prev_window:
        window_count += 1

print(window_count)
