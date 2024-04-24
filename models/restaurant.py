# models/restaurant.py
from app import db

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    address = db.Column(db.String(100))

    def __repr__(self):
        return f"<Restaurant {self.name}>"
