import pytest
import sys
from flask import Flask

sys.path.append("../chess_class/")
sys.path.append("../")
from board import Board
import chess_class


# figure movements on empty board


def test_emptyBoard_King_moves():
    chessboard = Board()
    chessboard.place_piece("E4", "King")
    king = chess_class.King("E1", chessboard.board)
    moves = king.list_available_moves()
    assert moves == ["d1", "d2", "e2", "f1", "f2"]


def test_emptyBoard_Queen_moves():
    chessboard = Board()
    chessboard.place_piece("D1", "Queen")
    queen = chess_class.Queen("D1", chessboard.board)
    assert queen.list_available_moves() == [
        "a1",
        "b1",
        "c1",
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
        "e2",
        "f3",
        "g4",
        "h5",
    ]


def test_emptyBoard_Rook_moves():
    chessboard = Board()
    rook = chess_class.Rook("A1", chessboard.board)
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
    bishop = chess_class.Bishop("C1", chessboard.board)
    chessboard.place_piece("C1", "Bishop")
    assert bishop.list_available_moves() == ['b2', 'a3', 'd2', 'e3', 'f4', 'g5', 'h6']


def test_emptyBoard_Knight_moves():
    chessboard = Board()
    knight = chess_class.Knight("B1", chessboard.board)
    chessboard.place_piece("B1", "Knight")
    assert knight.list_available_moves() == ['d2', 'c3', 'a3']


def test_emptyBoard_Pawns_moves():
    chess_board = Board()
    pawn = chess_class.Pawns("A2", chess_board.board)
    chess_board.place_piece("A2", "Pawn")
    assert pawn.list_available_moves() == ["a3", "a4"]


# figure movements on not empty board


def test_not_emptyBoard_King_moves():
    chess_board = Board()
    king = chess_class.King("E1")
    chess_board.place_piece("F1", "Bishop")
    chess_board.place_piece("D1", "Queen")
    chess_board.place_piece("E1", "King")
    assert king.list_available_moves() == ["E2"]


def test_not_emptyBoard_Queen_moves():
    chess_board = Board()
    queen = chess_class.Queen("D1")
    chess_board.place_piece("D1", "Queen")
    chess_board.place_piece("C1", "Bishop")
    chess_board.place_piece("E1", "King")
    assert queen.list_available_moves() == [
        "D2",
        "D3",
        "D4",
        "D5",
        "D6",
        "D7",
        "D8",
    ]


def test_not_emptyBoard_Rook_moves():
    chess_board = Board()
    rook = chess_class.Rook("A1")
    chess_board.place_piece("A1", "Rook")
    chess_board.place_piece("A5", "Pawn")
    chess_board.place_piece("G1", "Knight")
    assert rook.list_available_moves() == [
        "A2",
        "A3",
        "A4",
        "B1",
        "C1",
        "D1",
        "E1",
        "F1",
    ]


def test_not_emptyBoard_Bishop_moves():
    chess_board = Board()
    bishop = chess_class.Bishop("C1")
    chess_board.place_piece("C1", "Bishop")
    chess_board.place_piece("A3", "Pawn")
    chess_board.place_piece("F4", "Pawn")
    assert bishop.list_available_moves() == ["B2", "D2", "E3"]


def test_not_emptyBoard_Knight_moves():
    chess_board = Board()
    knight = chess_class.Knight("B1")
    chess_board.place_piece("B1", "Knight")
    chess_board.place_piece("A3", "Pawn")
    chess_board.place_piece("C3", "Pawn")

    assert knight.list_available_moves() == ["D2"]


def test_not_emptyBoard_Pawns_moves():
    chess_board = Board()
    pawn = chess_class.Pawns("A2")
    chess_board.place_piece("A2", "Pawn")
    chess_board.place_piece("A3", "Bishop")
    assert pawn.list_available_moves() == []


# validate move test


def test_validate_move_King():
    chess_board = Board()
    king = chess_class.King("E1")
    chess_board.place_piece("E1", "King")
    chess_board.place_piece("F1", "Bishop")
    chess_board.place_piece("D1", "Queen")
    assert king.validate_move("E2") is True
    assert king.validate_move("F1") is False


def test_validate_move_Queen():
    chess_board = Board()
    queen = chess_class.Queen("D1")
    chess_board.place_piece("D1", "Queen")
    chess_board.place_piece("C1", "Bishop")
    chess_board.place_piece("E1", "King")
    assert queen.validate_move("D2") is True
    assert queen.validate_move("C1") is False


def test_validate_move_Rook():
    chess_board = Board()
    rook = chess_class.Rook("A1")
    chess_board.place_piece("A1", "Rook")
    chess_board.place_piece("A5", "Pawn")
    chess_board.place_piece("G1", "Knight")
    assert rook.validate_move("A2") is True
    assert rook.validate_move("A5") is False


def test_validate_move_Bishop():
    chess_board = Board()
    bishop = chess_class.Bishop("C1")
    chess_board.place_piece("C1", "Bishop")
    chess_board.place_piece("A3", "Pawn")
    chess_board.place_piece("F4", "Pawn")
    assert bishop.validate_move("B2") is True
    assert bishop.validate_move("F4") is False


def test_validate_move_Knight():
    chess_board = Board()
    knight = chess_class.Knight("B1")
    chess_board.place_piece("B1", "Knight")
    chess_board.place_piece("A3", "Pawn")
    chess_board.place_piece("C3", "Pawn")
    assert knight.validate_move("D2") is True
    assert knight.validate_move("C2") is False


def test_validate_move_Pawns():
    chess_board = Board()
    pawn = chess_class.Pawns("A2")
    chess_board.place_piece("A2", "Pawn")
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
