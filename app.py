# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mypizzaapp.db'  # Adjust the URI as needed
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from routes import restaurant_routes



app.register_blueprint(restaurant_routes)


if __name__ == '__main__':
    app.run(debug=True)

