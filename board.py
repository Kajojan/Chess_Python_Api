class Board:
    def __init__(self):
        self.board = [[" " for _ in range(8)] for _ in range(8)]

    def place_piece(self, position , piece):
        col, row = position[0], int(position[1:])
        col = col.lower()
        if len(col) == 1 and "a" <= col <= "h":
            col = ord(col) - ord("a")
        else:
            raise ValueError("Invalid column value.")

        self.board[row - 1][col] = piece
