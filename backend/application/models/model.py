from datetime import datetime
from application import db


class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text())
    create_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, title, body) -> None:
        self.title = title
        self.body = body
