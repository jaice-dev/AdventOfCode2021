with open('input.txt') as file:
    input = [" ".join(line.split()) for line in file.readlines()]
    draws = [int(num) for num in input[0].split(",")]
    boards = []

    start = 2
    end = 7
    while end <= len(input):
        board = []
        board += input[start:end]
        board = [[[int(num), 0] for num in line.split(" ")] for line in board]
        boards.append(board)
        start += 6
        end += 6


def check_board_for_win(board):
    # Check vertical
    for line in board:
        sum = 0
        for num in line:
            sum += num[1]
        if sum == 5:
            return True

    # Check horizontal
    for i in range(0, 5):
        sum = 0
        for line in board:
            sum += line[i][1]
        if sum == 5:
            return True

    return False


def get_last_winning_board():
    winning_boards = []
    for num in draws:
        for board in boards:
            if boards.index(board) in winning_boards:
                continue
            for line in board:
                for value in line:
                    if num == value[0]:
                        value[1] = 1
            if check_board_for_win(board):
                winning_boards.append(boards.index(board))
                if len(winning_boards) == len(boards):
                    print(board)
                    unmarked_numbers = [num[0] for line in board for num in line if num[1] == 0]
                    marked_numbers = [num[0] for line in board for num in line if num[1] == 1]
                    sum_unmarked = sum(unmarked_numbers)
                    print(f"Sum of unmarked numbers: {sum_unmarked}")
                    print(f"Number just called: {num}")
                    print(f"Final score: {sum_unmarked * num}")


get_last_winning_board()
