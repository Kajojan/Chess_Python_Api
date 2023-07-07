from flask import Flask

from chess_class.chess_class import King
from board import Board

app = Flask(__name__)

@app.route('/')
def index():
    chessboard = Board()
    chessboard.place_piece( "E4", "King")
    chessboard.place_piece( "E3", "King")

    ches= King("E4", chessboard.board)
    return f" move: {ches.list_available_moves()}, move: {ches.validate_move('D3') }"

if __name__ == '__main__':
    app.run(port=8000)
