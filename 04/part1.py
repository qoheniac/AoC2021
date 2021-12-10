from numpy import array, logical_not, full


# board class holds board and keeps track of hits
class Board:
    def __init__(self, board):
        self._board = array(
            [
                [int(num) for num in line.split()]
                for line in board.rstrip().split("\n")
            ]
        )
        self._hits = full(self._board.shape, False)

    # check for hit and calculate score in case of bingo
    def update(self, number):
        self._hits[self._board == number] = True
        for axis in range(2):
            if (self._hits.sum(axis=axis) == 5).any():
                return number * self._board[logical_not(self._hits)].sum()
        return None


# read input
with open("input", "r") as f:
    numbers, *boards = f.read().split("\n\n")
numbers = [int(n) for n in numbers.split(",")]
boards = [Board(board) for board in boards]

# call numbers
for number in numbers:
    for board in boards:
        score = board.update(number)
        if score is not None:
            print(score)
            break
    else:
        continue
    break
