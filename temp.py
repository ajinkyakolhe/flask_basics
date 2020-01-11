# from flask import Flask, render_template, make_response
#
# app = Flask(__name__, template_folder="templates")

# @app.route("/")
# def users():
#     headers = {"Content-Type": "application/json"}
#     return make_response('Test worked!', 200, headers=headers)

from flask import Flask, make_response
app = Flask(__name__)

@app.route("/")
def home():
    headers = {"Content-Type": "application/json"}
    return make_response('Test worked!',
                         200,
                         headers=headers)

if __name__ == '__main__':
    app.run()
