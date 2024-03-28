from flask import Flask, request, render_template
from waitress import serve

app = Flask(__name__)

@app.route("/")
def index():
    home = "Home"
    return render_template("index.html",
                           home=home)

@app.route("/about")
def about_page():
    about = "About"
    return render_template("about.html",
                           about=about)

@app.route("/newsletter")
def newsletter_page():
    newsletter = "newsletter"
    return render_template("newsletter.html",
                           newsletter=newsletter)


@app.route("/porksinigang")
def pork_sinigang():
    return render_template("foods_templates/porksinigang.html")

@app.route("/cheesenoodles")
def cheese_noodles():
    return render_template("foods_templates/cheesenoodles.html")

@app.route("/schnitzel")
def schnitzel():
    return render_template("foods_templates/schnitzel.html")

@app.route("/restaurant-reviews")
def restaurant_reviews():
    return render_template("restaurantReviews.html")

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
