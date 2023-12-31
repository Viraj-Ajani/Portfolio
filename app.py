import os
from flask_mail import Mail, Message
from flask import Flask, render_template, redirect, request, make_response

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/about", methods=["GET", "POST"])
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("contact.html")

@app.route("/portfolio", methods=["GET", "POST"])
def portfolio():
    return render_template("portfolio.html")

@app.route("/resume", methods=["GET", "POST"])
def resume():
    if request.method == "POST":
        response = make_response(open("Viraj Ajani Resume.pdf", "rb").read())
        response.headers["Content-Disposition"] = "attachment; filename=Viraj Ajani Resume.pdf"
        return response
    return render_template("resume.html")

if __name__ == "__main__":
    app.run()
