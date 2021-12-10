with open('input.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

symbols = {
    "{": "}",
    "[": "]",
    "(": ")",
    "<": ">"
}

scores = {
    "{": 3,
    "[": 2,
    "(": 1,
    "<": 4
}


def is_corrupted(line):
    queue = []
    for char in line:
        if len(queue) == 0:
            queue += char
        elif symbols[queue[-1]] == char:
            queue.pop()
        elif char in symbols.values():
            return True
        elif char in ["(", "[", "{", "<"]:
            queue += char
    return queue

incomplete = []
for line in lines:
    queue = is_corrupted(line)
    if queue != True:
        incomplete.append(list(reversed(queue)))

final_score = []
for line in incomplete:
    local_score = 0
    for char in line:
        local_score *= 5
        local_score += scores[char]
    final_score.append(local_score)

middleIndex = int((len(final_score) - 1)/2)
final_score.sort()
print(final_score[middleIndex])
