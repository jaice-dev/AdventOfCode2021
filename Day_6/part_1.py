with open('input.txt') as file:
    lines = file.readlines()
    lines = [int(num) for line in lines for num in line.split(",")]

print(lines)

day = 0
while day < 80:
    for i in range(len(lines)):
        lines[i] -= 1
        if lines[i] < 0:
            lines[i] = 6
            lines.append(8)
    day += 1
    print(f"Day {day}: {lines}")

print(f"Lanternfish on day 80 = {len(lines)}")


