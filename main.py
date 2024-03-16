from flask import Flask, request, render_template
from waitress import serve

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
