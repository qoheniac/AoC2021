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
boards = array([Board(board) for board in boards])

# play until only one board has no bingo
playing = full(boards.shape, True)
while sum(playing) != 1:
    number = numbers.pop(0)
    playing[playing] = [
        board.update(number) is None for board in boards[playing]
    ]
last_board = boards[playing][0]

# play until the last board has bingo
for number in numbers:
    score = last_board.update(number)
    if score is not None:
        print(score)
        break
