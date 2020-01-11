from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, this is the first page <h1>Hey</h1>"



@app.route("/admin")
def admin():
    return redirect(url_for("home"))

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

if __name__ == "__main__":
    app.run()
