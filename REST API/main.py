from flask import Flask, render_template, request
from dbBrain import dbBrain
import models

app = Flask(__name__)

db = dbBrain(db_path='sqlite:///day_66_REST_API/cafes.db', tables=models)


@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/random")
def random():
    return f"{db.random_row(models.Cafe).name}"

@app.route("/all")
def all():
    return db.all_json(models.Cafe)

@app.route("/search")
def search():
    return db.search(models.Cafe, request.args.to_dict())

@app.route("/add", methods=['PATCH', 'GET', 'POST'])
def add(): 
    return db.add_row(models.Cafe, request.args.to_dict()) 

@app.route("/update", methods=['PATCH', 'GET', 'POST'])
def update():
    content = request.args.to_dict()
    if "id" in content:
        return db.patch_by_id(models.Cafe, content["id"], content)
    else:
     return "id not specified"
 
@app.route("/delete", methods=['DELETE'])
def delete(): 
    if request.args.get("id") is None:
        return "id not specified"
    if request.args.get("api_key") == "key":
        return db.delete_by_id(models.Cafe, request.args.get("id"))
    else:
        return "Permission denied", 503

if __name__ == '__main__':
    app.run(debug=True)