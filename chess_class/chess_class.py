from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, position):
        self.position = position

    @abstractmethod
    def list_available_moves() -> list:
        return []

    @abstractmethod
    def validate_move(dest_field) -> list:
        return []


class King(Figure):
    def list_available_moves() -> list:
        return []

    def validate_move(dest_field) -> list:
        return []


class Queen(Figure):
    def list_available_moves() -> list:
        return []

    def validate_move(dest_field) -> list:
        return []


class Rook(Figure):
    def list_available_moves() -> list:
        return []

    def validate_move(dest_field) -> list:
        return []


class Bishop(Figure):
    def list_available_moves() -> list:
        return []

    def validate_move(dest_field) -> list:
        return []


class Knight(Figure):
    def list_available_moves() -> list:
        return []

    def validate_move(dest_field) -> list:
        return []


class Pawns(Figure):
    def list_available_moves() -> list:
        return []

    def validate_move(dest_field) -> list:
        return []
