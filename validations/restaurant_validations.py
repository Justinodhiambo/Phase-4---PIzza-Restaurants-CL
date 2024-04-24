# validations/restaurant_validations.py
def validate_restaurant_name(name):
    return len(name) <= 50
