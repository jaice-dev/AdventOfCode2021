with open('input.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


gamma = ""
epsilon = ""
for i in range(0, len(lines[0])):
    bits = []
    for line in lines:
        bits.append(line[i])
    gamma += max(set(bits), key=bits.count)
    epsilon += min(set(bits), key=bits.count)
print(gamma)
print(int(gamma, 2))
print(epsilon)
print(int(epsilon, 2))
print(f"Power Consumption: {int(gamma, 2) * int(epsilon, 2)}")

# Part 2

"""
Next, you should verify the life support rating, 
which can be determined by multiplying the oxygen 
generator rating by the CO2 scrubber rating.
"""

oxygen_lines = lines.copy()
i = 0
while len(oxygen_lines) != 1:
    bits = []
    for line in oxygen_lines:
        bits += line[i]
    no_0s = bits.count('0')
    no_1s = bits.count('1')
    most_common = '1' if no_1s >= no_0s else '0'
    oxygen_lines = [newLine for newLine in oxygen_lines if newLine[i] == most_common]
    i += 1


co2_lines = lines.copy()
i = 0
while len(co2_lines) != 1:
    bits = []
    for line in co2_lines:
        bits += line[i]
    no_0s = bits.count('0')
    no_1s = bits.count('1')
    least_common = '0' if no_1s >= no_0s else '1'
    co2_lines = [newLine for newLine in co2_lines if newLine[i] == least_common]
    i += 1

print(f"Oxygen: {int(oxygen_lines[0], 2)}")
print(f"CO2: { int(co2_lines[0], 2)}")
print(f"Life Support Rating: {int(oxygen_lines[0], 2) * int(co2_lines[0], 2)}")

