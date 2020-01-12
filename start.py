"""
A Flask python program that creates routes for three different types
of pages with the help of Flask web framework
"""

from flask import Flask, redirect, url_for

# Creating an object for using the Flask module
app = Flask(__name__)


@app.route("/")
def home():
    """Returns a string on the home page"""
    return "Hello, this is the first page <h1>Hey</h1>"


@app.route("/admin")
def admin():
    """Redirects the admin page to the home page
    :rtype: webpage
    """
    return redirect(url_for("home"))


@app.route("/<name>")
def user(name):
    """Returns the string from the page name provided"""
    return f"Hello {name}!"


# Main function to run the Flask app
if __name__ == "__main__":
    app.run()
