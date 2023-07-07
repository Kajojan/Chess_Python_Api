from abc import ABC, abstractmethod


def getRowCol(position):
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
    return col, row - 1


class Figure(ABC):
    def __init__(self, position):
        self.position = position

    @abstractmethod
    def list_available_moves() -> list:
        return []

    @abstractmethod
    def validate_move(dest_field) -> bool:
        True


class King(Figure):
    def __init__(self, position, board):
        super().__init__(position)
        self.board = board

    def list_available_moves(self) -> list:
        col, row = getRowCol(self.position)
        print(self.position, col, row)
        possible_moves = []
        print("hello")
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                new_col = col + dx
                new_row = row + dy
                new_position = chr(new_col + ord("a")) + str(new_row + 1)
                if (
                    0 <= new_col <= 8
                    and 0 <= new_row <= 8
                    and self.board[new_row][new_col] == " "
                ):
                    possible_moves.append(new_position)
        return possible_moves

    def validate_move(self, dest_field) -> bool:
        posible_move = self.list_available_moves()
        dest_field = dest_field.lower()
        if dest_field in posible_move:
            return "valid"
        else:
            return "invalid"


class Queen(Figure):
    def __init__(self, position, board):
        super().__init__(position)
        self.board = board

    def list_available_moves(self) -> list:
        col, row = getRowCol(self.position)
        print(self.position, col, row)
        possible_moves = []

        for c in range(8):
            if c != col:
                if self.board[row][c] == " ":
                    new_position = chr(c + ord("a")) + str(row + 1)
                    possible_moves.append(new_position)

        for r in range(8):
            if r != row:
                if self.board[r][col] == " ":
                    new_position = chr(col + ord("a")) + str(r + 1)
                    possible_moves.append(new_position)

        # Poruszanie się po przekątnych
        for dx in range(-8, 9):
            if dx != 0:
                if 0 <= row + dx <= 7 and 0 <= col + dx <= 7:
                    print(row + dx, col + dx)
                    if self.board[row + dx][col + dx] == " ":
                        new_position = chr(col + dx + ord("a")) + str(row + dx + 1)
                        possible_moves.append(new_position)

        for dy in range(-8, 9):
            if dy != 0:
                if 0 <= row + dx <= 7 and 0 <= col + dx <= 7:
                    if self.board[row - dy][col + dx] == " ":
                        new_position = chr(col + dx + ord("a")) + str(row - dy + 1)
                        possible_moves.append(new_position)

        print(possible_moves)
        return possible_moves

    def validate_move(dest_field) -> bool:
        True


class Rook(Figure):
    def __init__(self, position):
        super().__init__(position)

    def list_available_moves(self) -> list:
        return []

    def validate_move(dest_field) -> bool:
        True


class Bishop(Figure):
    def __init__(self, position):
        super().__init__(position)

    def list_available_moves(self) -> list:
        return []

    def validate_move(dest_field) -> bool:
        True


class Knight(Figure):
    def __init__(self, position):
        super().__init__(position)

    def list_available_moves(self) -> list:
        return []

    def validate_move(dest_field) -> bool:
        True


class Pawns(Figure):
    def __init__(self, position):
        super().__init__(position)

    def list_available_moves(self) -> list:
        return []

    def validate_move(dest_field) -> bool:
        True
