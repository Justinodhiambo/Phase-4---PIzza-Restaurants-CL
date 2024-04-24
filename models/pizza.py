# models/pizza.py
from app import db

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    ingredients = db.Column(db.String(100))

    def __repr__(self):
        return f"<Pizza {self.name}>"
