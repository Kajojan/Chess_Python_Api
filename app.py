from flask import Flask

from board import Board

app = Flask(__name__)
chessboard = Board()
chessboard.place_piece("E4", "King")
chessboard.place_piece("E3", "King")


@app.route("/api/v1/<chess_figure>/<current_field>/")
def aviablemoves(chess_figure, current_field):
    figure_class = globals()[chess_figure.lower().capitalize()]
    ches = figure_class(f"{current_field}", chessboard.board)
    return {
        "availableMoves": list(ches.list_available_moves()),
        "error": None,
        "figure": chess_figure,
        "current_field": current_field,
    }


if __name__ == "__main__":
    app.run(port=8000)
