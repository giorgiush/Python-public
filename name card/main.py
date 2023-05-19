from flask import Flask
from flask import send_file


app = Flask(__name__)


@app.route("/")
def homepage():
    return send_file("templates/index.html")


if __name__ == "__main__":
    app.run(debug=True)