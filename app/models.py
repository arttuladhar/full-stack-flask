from .extensions import db

class User(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def serialize(self):
        return {
            "id": self.id, "username": self.username, "email": self.email
        }

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000), nullable=False)
