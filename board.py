from chess_class.chess_class import *
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
    def create(self):
        self.place_piece("E1", King("E1", self.board))
        self.place_piece("E8",King("E8", self.board))

        self.place_piece("D1",  Queen("D1", self.board))
        self.place_piece("D8",  Queen("D8", self.board))

        self.place_piece("C1",  Bishop("C1", self.board))
        self.place_piece("F1",  Bishop("F1", self.board))
        self.place_piece("C8",  Bishop("C8", self.board))
        self.place_piece("F8",  Bishop("F8", self.board))

        self.place_piece("B1",  Knight("B1", self.board))
        self.place_piece("G1",  Knight("G1", self.board))
        self.place_piece("B8", Knight("B8", self.board))
        self.place_piece("G8",  Knight("G8", self.board))

        self.place_piece("A1",  Rook("A1", self.board))
        self.place_piece("H1",  Rook("H1", self.board))
        self.place_piece("A8",  Rook("A8", self.board))
        self.place_piece("H8",  Rook("H8", self.board))

        white_pawns = (
        'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2')

        black_pawns = [
            'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7'
        ]
      
        for i in range(0,8):
            self.place_piece(f"{white_pawns[i]}",  Pawns(white_pawns[i], self.board))
            self.place_piece(f"{black_pawns[i]}",  Pawns(black_pawns[i], self.board))
    
    





        
