with open('input.txt') as file:
    lines = file.readlines()
    lines = [[line.split(" | ")[0].split(" "), line.split(" | ")[1].rstrip().split(" ")] for line in lines]

total = 0
for line in lines:
    # print(line)
    unique_combinations = set(line[0])
    combinations = {}

    # for comb in unique_combinations:
    #     if len(comb) == 2:
    #         combinations[1] = comb
    #     if len(comb) == 4:
    #         combinations[4] = comb
    #     if len(comb) == 3:
    #         combinations[7] = comb
    #     if len(comb) == 7:
    #         combinations[8] = comb
    combinations[1] = [comb for comb in unique_combinations if len(comb) == 2][0]
    combinations[7] = [comb for comb in unique_combinations if len(comb) == 3][0]
    combinations[4] = [comb for comb in unique_combinations if len(comb) == 4][0]
    combinations[8] = [comb for comb in unique_combinations if len(comb) == 7][0]

    zero_nine_six = [comb for comb in unique_combinations if len(comb) == 6]
    for num in zero_nine_six:
        if len(set(num).intersection(set(combinations[1]))) == 1:
            combinations[6] = num
        elif len(set(num).difference(set(combinations[4]))) == 2:
            combinations[9] = num
        else:
            combinations[0] = num

    two_three_five = [comb for comb in unique_combinations if len(comb) == 5]
    for num in two_three_five:
        if len(set(num).difference(set(combinations[1]))) == 3:
            combinations[3] = num
        elif len(set(num).difference(set(combinations[4]))) == 2:
            combinations[5] = num
        else:
            combinations[2] = num

    output = ""
    for num in line[1]:
        for key , value in combinations.items():
            if set(value) == set(num):
                output += str(key)
    total += int(output)

print(total)


