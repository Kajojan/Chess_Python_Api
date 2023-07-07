from flask import Flask
from db.database import db
from db.models import Chessboard
from chess_class.chess_class import King

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chess.db'

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    chessboard = Chessboard(position='A1', piece='rook')
    ches= King("E4")
    db.session.add(chessboard)
    db.session.commit()
    chessboard = Chessboard.query.first()
    return f"Chessboard position: {chessboard.position}, piece: {chessboard.piece}, move: {ches.list_available_moves()}"

if __name__ == '__main__':
    app.run(port=8000)
