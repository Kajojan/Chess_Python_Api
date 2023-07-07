import pytest
import sys
import board
import chess_class

sys.path.append("../chess_class/")


# figure movements on empty board


def test_emptyBoard_King_moves():
    chess_board = board.Board()
    king = chess_class.King("E1")
    chess_board.place_piece("E1", "King")
    assert king.list_available_moves() == ["E2", "F1", "D1"]


def test_emptyBoard_Queen_moves():
    chess_board = board.Board()
    queen = chess_class.Queen("D1")
    chess_board.place_piece("D1", "Queen")
    assert queen.list_available_moves() == [
        "D2",
        "D3",
        "D4",
        "D5",
        "D6",
        "D7",
        "D8",
        "A1",
        "B1",
        "C1",
        "E1",
        "F1",
        "G1",
        "H1",
        "A4",
        "B3",
        "C2",
        "E2",
        "F3",
        "G4",
        "H5",
    ]


def test_emptyBoard_Rook_moves():
    chess_board = board.Board()
    rook = chess_class.Rook("A1")
    chess_board.place_piece("A1", "Rook")
    assert rook.list_available_moves() == [
        "A2",
        "A3",
        "A4",
        "A5",
        "A6",
        "A7",
        "A8",
        "B1",
        "C1",
        "D1",
        "E1",
        "F1",
        "G1",
        "H1",
    ]


def test_emptyBoard_Bishop_moves():
    chess_board = board.Board()
    bishop = chess_class.Bishop("C1")
    chess_board.place_piece("C1", "Bishop")
    assert bishop.list_available_moves() == ["A3", "B2", "D2", "E3", "F4", "G5", "H6"]


def test_emptyBoard_Knight_moves():
    chess_board = board.Board()
    knight = chess_class.Knight("B1")
    chess_board.place_piece("B1", "Knight")
    assert knight.list_available_moves() == ["A3", "C3", "D2"]


def test_emptyBoard_Pawns_moves():
    chess_board = board.Board()
    pawn = chess_class.Knight("A2")
    chess_board.place_piece("A2", "Pawn")
    assert pawn.list_available_moves() == ["A3"]


# figure movements on not empty board


def test_not_emptyBoard_King_moves():
    chess_board = board.Board()
    king = chess_class.King("E1")
    chess_board.place_piece("F1", "Bishop")
    chess_board.place_piece("D1", "Queen")
    assert king.list_available_moves() == ["E2"]


def test_not_emptyBoard_Queen_moves():
    chess_board = board.Board()
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
    chess_board = board.Board()
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
    chess_board = board.Board()
    bishop = chess_class.Bishop("C1")
    chess_board.place_piece("C1", "Bishop")
    chess_board.place_piece("A3", "Pawn")
    chess_board.place_piece("F4", "Pawn")
    assert bishop.list_available_moves() == ["B2", "D2", "E3"]


def test_not_emptyBoard_Knight_moves():
    chess_board = board.Board()
    knight = chess_class.Knight("B1")
    chess_board.place_piece("B1", "Knight")
    chess_board.place_piece("A3", "Pawn")
    chess_board.place_piece("C3", "Pawn")

    assert knight.list_available_moves() == ["D2"]


def test_not_emptyBoard_Pawns_moves():
    chess_board = board.Board()
    pawn = chess_class.Knight("A2")
    chess_board.place_piece("A2", "Pawn")
    chess_board.place_piece("A3", "Bishop")
    assert pawn.list_available_moves() == []
