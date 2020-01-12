"""
A Flask program that uses render_template method to
implement a for loop inside the index HTML page.

"""

from flask import Flask, render_template

# Creating an object for using the Flask module
app = Flask(__name__)

@app.route("/<name>")
def home(name):
    """Returns a rendered HTML page with Python code in index.html"""
    return render_template("index.html", content=name)

# Main function to run the Flask app
if __name__ == "__main__":
    app.run()