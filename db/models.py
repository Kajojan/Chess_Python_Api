from db.database import db

class Chessboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.String(2), nullable=False)
    piece = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Chessboard position='{self.position}' piece='{self.piece}'>"
