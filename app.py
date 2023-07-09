from flask import Flask, make_response
from chess_class.chess_class import King, Queen, Rook, Knight, Pawns, Bishop
from board import Board

app = Flask(__name__)
chessboard = Board()
chessboard.place_piece("E4", "King")
chessboard.place_piece("E3", "King")


@app.route("/api/v1/<chess_figure>/<current_field>/")
def aviablemoves(chess_figure, current_field):
    try:
        figure_class = globals()[chess_figure.lower().capitalize()]
    except KeyError:
        status_code = 404
        error = f"Class '{chess_figure}' not found"
        aviablemoves = []
    else:
        try:
            figure_class = globals()[chess_figure.lower().capitalize()]
            ches = figure_class(f"{current_field}", chessboard.board)
            aviablemoves = list(ches.list_available_moves())
            error = None
            status_code = 200
        except ValueError as err:
            aviablemoves = []
            status_code = 409
            error = str(err)

    response = make_response(
        {
            "availableMoves": aviablemoves,
            "error": error,
            "figure": chess_figure,
            "currentField": current_field,
        }
    )
    response.status_code = status_code

    print(response)
    return response


if __name__ == "__main__":
    app.run(port=8000)
