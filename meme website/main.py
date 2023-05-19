from flask import Flask, render_template, redirect, url_for, request
import requests


app = Flask(__name__)


@app.route('/')
def home():
    resp = requests.get('https://meme-api.com/gimme').json()
    return render_template('index.html', meme = resp["url"])


@app.route('/generate', methods=['POST'])
def generate():
    if request.method == "POST":
        return redirect(url_for('home'))
    
    
if __name__ == "__main__":
    app.run(debug=True)