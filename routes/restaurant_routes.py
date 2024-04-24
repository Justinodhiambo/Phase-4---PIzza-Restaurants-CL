# routes/restaurant_routes.py
from flask import Blueprint, jsonify
from models.restaurant import Restaurant

restaurant_routes = Blueprint('restaurant_routes', __name__)

@restaurant_routes.route('/restaurants')
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([restaurant.serialize() for restaurant in restaurants])

