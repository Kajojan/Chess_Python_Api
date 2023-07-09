from flask import Flask, make_response
from chess_class.chess_class import King, Queen, Rook, Knight, Pawns, Bishop
from board import Board

app = Flask(__name__)
chessboard = Board()
# chessboard.create()


@app.route("/api/v1/<chess_figure>/<current_field>")
def aviablemoves(chess_figure, current_field):
    try:
        figure_class = globals()[chess_figure.lower().capitalize()]
    except KeyError:
        status_code = 404
        error = f"Figure '{chess_figure}' not found"
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


@app.route("/api/v1/<chess_figure>/<current_field>/<dest_field>")
def valid(chess_figure, current_field, dest_field):
    try:
        figure_class = globals()[chess_figure.lower().capitalize()]
    except KeyError:
        status_code = 404
        error = f"Class '{chess_figure}' not found"
        move = "invalid"
    else:
        try:
            figure_class = globals()[chess_figure.lower().capitalize()]
            ches = figure_class(f"{current_field}", chessboard.board)
            print(ches.validate_move(dest_field))
            if ches.validate_move(dest_field):
                status_code = 200
                error = None
                move = "valid"
            else:
                status_code = 409
                error = "Current move is not permitted."
                move = "invalid"

        except ValueError as err:
            move = "invalid"
            status_code = 409
            error = str(err)

    response = make_response(
        {
            "move": move,
            "error": error,
            "figure": chess_figure,
            "currentField": current_field,
            "destField": dest_field,
        }
    )
    response.status_code = status_code

    return response


if __name__ == "__main__":
    app.run(port=8000)
