class Board:
    def __init__(self):
        self.board = [[" " for _ in range(8)] for _ in range(8)]

    def place_piece(self, position, piece):
        col, row = position[0], int(position[1:])
        col = col.lower()
        if (len(col) != 1 or col not in "abcdefgh") and (not (1 <= row <= 8)):
            raise ValueError("Invalid column and row values")
        elif len(col) != 1 or col not in "abcdefgh":
            raise ValueError("Invalid column value")
        elif not (1 <= row <= 8):
            raise ValueError("Invalid row value")
        else:
            col = ord(col) - ord("a")
        self.board[row - 1][col] = piece
