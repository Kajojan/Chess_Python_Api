import pytest
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)
from board import Board
from chess_class.chess_class import King, Queen, Rook, Knight, Pawns, Bishop


# figure movements on empty board


def test_emptyBoard_King_moves():
    chessboard = Board()
    chessboard.place_piece("E4", "King")
    king = King("E1", chessboard.board)
    moves = king.list_available_moves()
    assert moves == ["d1", "d2", "e2", "f1", "f2"]


def test_emptyBoard_Queen_moves():
    chessboard = Board()
    chessboard.place_piece("D1", "Queen")
    queen = Queen("D1", chessboard.board)
    assert queen.list_available_moves() == [
        "c1",
        "b1",
        "a1",
        "e1",
        "f1",
        "g1",
        "h1",
        "d2",
        "d3",
        "d4",
        "d5",
        "d6",
        "d7",
        "d8",
        "c2",
        "b3",
        "a4",
        "e2",
        "f3",
        "g4",
        "h5",
    ]


def test_emptyBoard_Rook_moves():
    chessboard = Board()
    rook = Rook("A1", chessboard.board)
    chessboard.place_piece("A1", "Rook")
    assert rook.list_available_moves() == [
        "b1",
        "c1",
        "d1",
        "e1",
        "f1",
        "g1",
        "h1",
        "a2",
        "a3",
        "a4",
        "a5",
        "a6",
        "a7",
        "a8",
    ]


def test_emptyBoard_Bishop_moves():
    chessboard = Board()
    bishop = Bishop("C1", chessboard.board)
    chessboard.place_piece("C1", "Bishop")
    assert bishop.list_available_moves() == ["b2", "a3", "d2", "e3", "f4", "g5", "h6"]


def test_emptyBoard_Knight_moves():
    chessboard = Board()
    knight = Knight("B1", chessboard.board)
    chessboard.place_piece("B1", "Knight")
    assert knight.list_available_moves() == ["d2", "c3", "a3"]


def test_emptyBoard_Pawns_moves():
    chess_board = Board()
    pawn = Pawns("A2", chess_board.board)
    chess_board.place_piece("A2", "Pawn")
    assert pawn.list_available_moves() == ["a3", "a4"]


# figure movements on not empty board


def test_not_emptyBoard_King_moves():
    chess_board = Board()
    chess_board.place_piece("F1", "Bishop")
    chess_board.place_piece("D1", "Queen")
    chess_board.place_piece("E1", "King")
    king = King("E1", chess_board.board)

    assert king.list_available_moves() == ["d2", "e2", "f2"]


def test_not_emptyBoard_Queen_moves():
    chess_board = Board()
    chess_board.place_piece("D1", "Queen")
    chess_board.place_piece("C1", "Bishop")
    chess_board.place_piece("E1", "King")
    queen = Queen("D1", chess_board.board)
    assert queen.list_available_moves() == [
        "d2",
        "d3",
        "d4",
        "d5",
        "d6",
        "d7",
        "d8",
        "c2",
        "b3",
        "a4",
        "e2",
        "f3",
        "g4",
        "h5",
    ]


def test_not_emptyBoard_Rook_moves():
    chess_board = Board()
    chess_board.place_piece("A1", "Rook")
    chess_board.place_piece("A5", "Pawn")
    chess_board.place_piece("G1", "Knight")
    rook = Rook("A1", chess_board.board)
    assert rook.list_available_moves() == [
        "b1",
        "c1",
        "d1",
        "e1",
        "f1",
        "a2",
        "a3",
        "a4",
    ]


def test_not_emptyBoard_Bishop_moves():
    chess_board = Board()
    chess_board.place_piece("C1", "Bishop")
    chess_board.place_piece("A3", "Pawn")
    bishop = Bishop("C1", chess_board.board)
    assert bishop.list_available_moves() == ["b2", "d2", "e3", "f4", "g5", "h6"]


def test_not_emptyBoard_Knight_moves():
    chess_board = Board()
    chess_board.place_piece("B1", "Knight")
    chess_board.place_piece("A3", "Pawn")
    chess_board.place_piece("C3", "Pawn")
    knight = Knight("B1", chess_board.board)
    assert knight.list_available_moves() == ["d2"]


def test_not_emptyBoard_Pawns_moves():
    chess_board = Board()
    chess_board.place_piece("A2", "Pawn")
    chess_board.place_piece("A3", "Bishop")
    pawn = Pawns("A2", chess_board.board)
    assert pawn.list_available_moves() == []


# validate move test


def test_validate_move_King():
    chess_board = Board()
    chess_board.place_piece("E1", "King")
    chess_board.place_piece("F1", "Bishop")
    chess_board.place_piece("D1", "Queen")
    king = King("E1", chess_board.board)
    assert king.validate_move("E2") is True
    assert king.validate_move("F1") is False


def test_validate_move_Queen():
    chess_board = Board()
    chess_board.place_piece("D1", "Queen")
    chess_board.place_piece("C1", "Bishop")
    chess_board.place_piece("E1", "King")
    queen = Queen("D1", chess_board.board)
    assert queen.validate_move("D2") is True
    assert queen.validate_move("C1") is False


def test_validate_move_Rook():
    chess_board = Board()

    chess_board.place_piece("A1", "Rook")
    chess_board.place_piece("A5", "Pawn")
    chess_board.place_piece("G1", "Knight")
    rook = Rook("A1", chess_board.board)
    assert rook.validate_move("A2") is True
    assert rook.validate_move("A5") is False


def test_validate_move_Bishop():
    chess_board = Board()
    chess_board.place_piece("C1", "Bishop")
    chess_board.place_piece("A3", "Pawn")
    chess_board.place_piece("F4", "Pawn")
    bishop = Bishop("C1", chess_board.board)
    assert bishop.validate_move("B2") is True
    assert bishop.validate_move("F4") is False


def test_validate_move_Knight():
    chess_board = Board()
    chess_board.place_piece("B1", "Knight")
    chess_board.place_piece("A3", "Pawn")
    chess_board.place_piece("C3", "Pawn")
    knight = Knight("B1", chess_board.board)
    assert knight.validate_move("D2") is True
    assert knight.validate_move("C2") is False


def test_validate_move_Pawns():
    chess_board = Board()
    chess_board.place_piece("A2", "Pawn")
    pawn = Pawns("A2", chess_board.board)

    assert pawn.validate_move("A3") is True
    assert pawn.validate_move("B2") is False


# board tests


def test_board_place_piece_invalid_column():
    with pytest.raises(ValueError) as erro:
        chess_board = Board()
        chess_board.place_piece("Z2", "Pawn")

    exception_message = str(erro.value)
    assert exception_message == "Invalid column value"


def test_board_place_piece_invalid_row():
    with pytest.raises(ValueError) as erro:
        chess_board = Board()
        chess_board.place_piece("A9", "Pawn")

    exception_message = str(erro.value)
    assert exception_message == "Invalid row value"


def test_board_place_piece_invalid_column_and_row():
    with pytest.raises(ValueError) as erro:
        chess_board = Board()
        chess_board.place_piece("Z9", "Pawn")

    exception_message = str(erro.value)
    assert exception_message == "Invalid column and row values"
