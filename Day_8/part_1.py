with open('input.txt') as file:
    lines = file.readlines()
    lines = [[line.split(" | ")[0].split(" "), line.split(" | ")[1].rstrip().split(" ")] for line in lines]

count = 0
for line in lines:
    # print(line)
    unique_combinations = set(line[0])
    combinations = {}

    for comb in unique_combinations:
        if len(comb) == 2:
            combinations["1"] = comb
        if len(comb) == 4:
            combinations["4"] = comb
        if len(comb) == 3:
            combinations["7"] = comb
        if len(comb) == 7:
            combinations["8"] = comb

    for num in line[1]:
        if set(num) in [set(combination) for combination in combinations.values()]:
            count += 1

print(count)

