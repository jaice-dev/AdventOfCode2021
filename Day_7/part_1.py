with open('input.txt') as file:
    lines = file.readlines()
    lines = [int(num) for line in lines for num in line.split(",")]

print(lines)

lowest_fuel = sum(lines) * sum(lines)
for i in range(min(lines), max(lines) + 1):
    total_fuel = 0
    for num in lines:
        dist = abs(num - i)
        total_fuel += (dist * (dist+1))/2
    #     n(n+1)/2
    if total_fuel < lowest_fuel:
        lowest_fuel = total_fuel

print(lowest_fuel)