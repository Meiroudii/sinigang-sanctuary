from flask import Flask, request, render_template 
from datetime import datetime
from waitress import serve

app = Flask(__name__)
# app.config['SUPER_KEY'] = "1234567890"

@app.route("/")
def index():
    home = "Home"
    return render_template("index.html",
                           home=home)

@app.route("/test/<test>")
def test(test):
    stuff = "This is <em>cool</em>"
    favorite_pizza = ["Pepperoni", "Macncheese", "Chocopiz"]
    return render_template("test.html", 
                           test=test, 
                           stuff=stuff,
                           favorite_pizza=favorite_pizza)

@app.route("/about")
def about_page():
    about = "About"
    return render_template("about.html",
                           about=about)

@app.route("/search")
def search():
    search = "search"
    foods = [
        "Schnitzel",
        "Käsespätzle",
        "Pork Sinigang"
    ]

    return render_template("search.html",
                           search=search,
                           foods=foods)

@app.route("/newsletter")
def newsletter_page():
    newsletter = "newsletter"
    return render_template("newsletter.html",
                           newsletter=newsletter)


@app.route("/porksinigang")
def pork_sinigang():
    return render_template("foods_templates/porksinigang.html")

@app.route("/kaesespaetzle")
def cheese_noodles():
    return render_template("foods_templates/cheesenoodles.html")

@app.route("/schnitzel")
def schnitzel():
    return render_template("foods_templates/schnitzel.html")

@app.route("/restaurant-reviews")
def restaurant_reviews():
    return render_template("restaurantReviews.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server(e):
    return render_template("500.html"), 500 

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
