from flask import Blueprint, render_template, current_app #, session

from app.models.food import Food

product_routes = Blueprint("product_routes", __name__)

@product_routes.route("/food")
def food():
    food = Food.all()
    return render_template("food.html", food=food)
