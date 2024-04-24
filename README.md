# Phase-4---PIzza-Restaurants-CL

Welcome to the Phase 4 Code Challenge for Pizza Restaurants! In this assessment, you'll be working with a Pizza Restaurant domain and building out a Flask API to add the functionality described below.

Models and Validations
A Restaurant has many Pizzas through RestaurantPizza.
A Pizza has many Restaurants through RestaurantPizza.
A RestaurantPizza belongs to a Restaurant and a Pizza.
Validation: Price for RestaurantPizza must be between 1 and 30.
Validation: Restaurant name must be unique and less than 50 characters.
Routes
GET /restaurants
Returns JSON data of all restaurants.
GET /restaurants/:id
Returns JSON data of a specific restaurant by ID along with its pizzas.
DELETE /restaurants/:id
Deletes a restaurant by ID along with associated RestaurantPizzas.
GET /pizzas
Returns JSON data of all pizzas.
POST /restaurant_pizzas
Creates a new RestaurantPizza associated with an existing Pizza and Restaurant.