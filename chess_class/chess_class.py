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

def add_possible_move_if_empty(row, col, possible_moves,board):
    if board[row][col] == " ":
        new_position = chr(col + ord("a")) + str(row + 1)
        possible_moves.append(new_position)
        return True
    else:
        print("fasle")
        return False


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

        # left
        for new_col in range(col - 1, -1, -1):
            new_position = chr(new_col + ord("a")) + str(row + 1)
            if 0 <= row  <= 7 and 0 <= new_col <= 7:
                   if not add_possible_move_if_empty(row,new_col,possible_moves,self.board):
                        break

        #right
        for new_col in range(col + 1, 8):
            new_position = chr(new_col + ord("a")) + str(row + 1)
            if 0 <= row  <= 7 and 0 <= new_col <= 7:
                if not add_possible_move_if_empty(row,new_col,possible_moves,self.board):
                        break

       #down
        for new_row in range(row - 1, -1, -1):
            new_position = chr(col + ord("a")) + str(new_row + 1)
            if 0 <= new_row  <= 7 and 0 <= col <= 7:
                    if not add_possible_move_if_empty(new_row,col,possible_moves,self.board):
                        break

        #up
        for new_row in range(row + 1, 8):
            new_position = chr(col + ord("a")) + str(new_row + 1)
            if 0 <= new_row  <= 7 and 0 <= col <= 7:
                   if not add_possible_move_if_empty(new_row,col,possible_moves,self.board):
                        break

        
        for i in range(1,8):
            #left-down
            if col - i >= 0 and row - i >= 0:
               if not add_possible_move_if_empty(row - i,col - i,possible_moves,self.board):
                        break
            #left-up
            if col - i >= 0 and row + i < 8:
                 if not add_possible_move_if_empty(row + i,col - i,possible_moves,self.board):
                        break
            #right-down
            if col + i < 8 and row - i >= 0:
                 if not add_possible_move_if_empty(row - i,col + i,possible_moves,self.board):
                        break
            #right-up
            if col + i < 8 and row + i < 8:
                  if not add_possible_move_if_empty(row + i,col + i,possible_moves,self.board):
                        break

        print(possible_moves)
        return possible_moves

    def validate_move(dest_field) -> bool:
        True


class Rook(Figure):
    def __init__(self, position,board):
        super().__init__(position)
        self.board = board

    def list_available_moves(self) -> list:
        col, row = getRowCol(self.position)
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

        print(possible_moves)
        return possible_moves
    def validate_move(dest_field) -> bool:
        True


class Bishop(Figure):
    def __init__(self, position, board):
        super().__init__(position)
        self.board=board

    def list_available_moves(self) -> list:
        col, row = getRowCol(self.position)
        possible_moves = []

        for i in range(1, 8):
            new_col = col - i
            new_row = row - i
            if new_col >= 0 and new_row >= 0:
                if self.board[new_row][new_col] == " ":
                    new_position = chr(new_col + ord("a")) + str(new_row + 1)
                    possible_moves.append(new_position)
            else:
                break

        for i in range(1, 8):
            new_col = col + i
            new_row = row - i
            if new_col <= 7 and new_row >= 0:
                 if self.board[new_row][new_col] == " ":
                    new_position = chr(new_col + ord("a")) + str(new_row + 1)
                    possible_moves.append(new_position)
            else:
                break
        
        for i in range(1, 8):
            new_col = col - i
            new_row = row + i
            if new_col >= 0 and new_row <= 7:
                if self.board[new_row][new_col] == " ":
                    new_position = chr(new_col + ord("a")) + str(new_row + 1)
                    possible_moves.append(new_position)
            else:
                break
        
        for i in range(1, 8):
            new_col = col + i
            new_row = row + i
            if new_col <= 7 and new_row <= 7:
                if self.board[new_row][new_col] == " ":
                    new_position = chr(new_col + ord("a")) + str(new_row + 1)
                    possible_moves.append(new_position)
            else:
                break
        print(possible_moves)
        return possible_moves

    def validate_move(dest_field) -> bool:
        True


class Knight(Figure):
    def __init__(self, position,board):
        super().__init__(position)
        self.board=board

    def list_available_moves(self) -> list:
        col, row = getRowCol(self.position)
        possible_moves = []
        moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

        for dx, dy in moves:
                   print(col, dx, row, dy)
                   new_col = col + dx
                   new_row = row + dy
                   if 0 <= new_col <= 7 and 0 <= new_row <= 7:
                       if self.board[new_row][new_col] == " ":
                            new_position = chr(new_col + ord("a")) + str(new_row + 1)
                            possible_moves.append(new_position)
        
        return possible_moves
    def validate_move(dest_field) -> bool:
        True


class Pawns(Figure):
    def __init__(self, position,board):
        super().__init__(position)
        self.board=board
    def list_available_moves(self) -> list:
        col, row = getRowCol(self.position)
        possible_moves = []
        if(row == 1):
            if self.board[row+1][col] == " ":
                            new_position = chr(col + ord("a")) + str(row+1 + 1)
                            possible_moves.append(new_position)
            if self.board[row+2][col] == " ":
                            new_position = chr(col + ord("a")) + str(row+2 + 1)
                            possible_moves.append(new_position)
        else:
            if self.board[row+1][col] == " ":
                            new_position = chr(col + ord("a")) + str(row+1 + 1)
                            possible_moves.append(new_position)
        return possible_moves
    def validate_move(dest_field) -> bool:
        True
