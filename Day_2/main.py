"""
forward X increases the horizontal position by X units.
down X increases the depth by X units.
up X decreases the depth by X units.

Note that since you're on a submarine, down and up affect your depth,
and so they have the opposite result of what you might expect.
"""

with open('input.txt') as file:
    lines = file.readlines()
    lines = [[line.rstrip().split()[0], int(line.rstrip().split()[1])] for line in lines]

horizontal_position = 0
depth = 0

for line in lines:
    if line[0] == 'forward':
        horizontal_position += line[1]
    if line[0] == 'down':
        depth += line[1]
    if line[0] == 'up':
        depth -= line[1]

print(f"Position: {horizontal_position}")
print(f"Depth: {depth}")
print(f"Pos x Depth: {horizontal_position * depth}")

# Part two
"""
down X increases your aim by X units.
up X decreases your aim by X units.
forward X does two things:
    It increases your horizontal position by X units.
    It increases your depth by your aim multiplied by X.
"""

horizontal_position = 0
depth = 0
aim = 0

for line in lines:
    if line[0] == 'forward':
        horizontal_position += line[1]
        depth += aim * line[1]
    if line[0] == 'down':
        aim += line[1]
    if line[0] == 'up':
        aim -= line[1]

print(f"Position: {horizontal_position}")
print(f"Depth: {depth}")
print(f"Aim: {aim}")
print(f"Pos x Depth: {horizontal_position * depth}")

