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

@app.route("/contact")
def contact_page():
    contact = "Contact"
    return render_template("contact.html",
                           contact=contact)

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
