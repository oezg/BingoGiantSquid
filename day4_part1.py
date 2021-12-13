import numpy as np

with open("bingo_day4") as inp:
    numbers = inp.readline()
    boards = inp.read()
numbers = [int(number) for number in numbers.rstrip().split(",")]
boards = boards.strip().split("\n\n")
boards = [[[int(x) for x in row.split()] for row in board.splitlines()] for board in boards]
boards = np.array(boards)


def bingo(board):
    return 0 in board.sum(axis=0) or 0 in board.sum(axis=1)

def mark(number, board):
    if number in board:
        index = np.where(board == number)
        board[index] = 0

def score(numbers, boards):
    for i, number in enumerate(numbers):
        for board in boards:
            mark(number, board)
            if bingo(board):
                return board.sum() * number

print(score(numbers, boards))