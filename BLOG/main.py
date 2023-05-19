from flask import Flask, render_template, request, flash
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, LoginManager, login_required, current_user, logout_user
from flask_gravatar import Gravatar
import datetime
import json
from flask import abort
from functools import wraps

from dbBrain import dbBrain
import models
import forms


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)
    return decorated_function


db = dbBrain(db_path='sqlite:///days_59_60_67_69_BLOG/blog.db', tables=models)

app = Flask(__name__)
Bootstrap(app)
ckeditor = CKEditor(app)
app.secret_key = "I made you read"


login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return db.get_object_by_id(models.Users, user_id)


gravatar = Gravatar(app, size=100, rating='g', default='retro', force_default=False, force_lower=False, use_ssl=False, base_url=None)


def create_app():
    
    @app.route('/register', methods = ['POST', 'GET'])
    def register():
        form = forms.Register()
        if form.validate_on_submit():
            if db.get_object_by_params(models.Users, {"email": form.data["email"]}) != "Not found":
                flash("You've already signed up with that email, log in instead!")
                return redirect(url_for('login'))
            db.add_row(models.Users, {"name": form.data["name"], "email": form.data["email"], "password": generate_password_hash(form.data["password"], method="pbkdf2:sha256", salt_length=8)})
            login_user(db.get_object_by_params(models.Users, {"email": form.data["email"]}))
            return redirect(url_for('homepage'))
        return render_template("register.html", form=form)


    @app.route('/login', methods = ['POST', 'GET'])
    def login():
        form = forms.Login()
        if form.validate_on_submit():
            user = db.get_object_by_params(models.Users, {"email": form.data["email"]})
            if user == "Not found":
                flash("Wrong email")
                return redirect(url_for('login'))
            else:
                if check_password_hash(user.password, form.data["password"]):
                    login_user(user)
                    return redirect(url_for('homepage'))
                else:
                    flash("Wrong password")
                    return redirect(url_for('login'))
        return render_template("login.html", form=form)


    @app.route('/logout', methods = ['POST', 'GET'])
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('homepage'))


    @app.route('/')
    def homepage():
        blogs = json.loads(db.all_json(models.Posts))
        authors = db.get_all_objects(models.Users)
        return render_template('index.html', blogs=blogs, authors=authors)


    @app.route('/about')
    def about():
        return render_template('about.html')


    @app.route('/contact', methods = ['POST', 'GET'])
    def contact():
        if request.method == 'POST':
            print(f"Name: {request.form['thename']}\nEmail: {request.form['theemail']}\nPhone: {request.form['thephonenumber']}\nMessage: {request.form['themessage']}")
            return render_template('contact.html', message_sent=True)
        return render_template('contact.html', message_sent=False)
            
            
    @app.route('/add', methods=['POST', 'GET'])
    @login_required
    @admin_only
    def add():
        form = forms.CreatePostForm()
        if form.validate_on_submit():
            content = {
                "title": form.title.data,
                "subtitle": form.subtitle.data,
                "date": datetime.datetime.today().strftime("%B %d, %Y"),
                "body": form.body.data,
                "author_id": current_user.id,
                "img_url": form.img_url.data 
                }
            db.add_row(models.Posts, content)
            return redirect(url_for('homepage'))
        return render_template('make-post.html', form=form)


    @app.route('/post/<int:id>', methods=['POST', 'GET'])
    @login_required
    def post(id):
        form = forms.Comment()
        comments = db.get_all_objects(models.Comments)
        comment_authors = db.get_all_objects(models.Users)
        if request.method == "POST":
            content = {
                        "text": form.body.data,
                        "author_id": current_user.id,
                        "post_id": id
                       }
            db.add_row(models.Comments, content)
            return redirect(url_for('post', id=id))
        return render_template('post.html', form=form, blog_post=json.loads(db.search(models.Posts, {"id": id}))[0], current_user=current_user, comments=comments, comment_authors=comment_authors)


    @app.route('/delete/<int:id>')
    @login_required
    @admin_only
    def delete(id):
        db.delete_by_id(models.Posts, id)
        return redirect(url_for('homepage'))


    @app.route('/edit/<int:id>', methods=['PATCH', 'POST', 'GET'])
    @login_required
    @admin_only
    def edit(id):
        post = json.loads(db.search(models.Posts, {"id": id}))[0]
        form = forms.CreatePostForm(title=post['title'], subtitle=post['subtitle'], img_url=post['img_url'], body=post['body'])
        if form.validate_on_submit():
            content = {            
                    "title": form.title.data,
                    "subtitle": form.subtitle.data,
                    "body": form.body.data,
                    "img_url": form.img_url.data 
                    }
            db.patch_by_id(models.Posts, id, content)
            return render_template('post.html', blog_post=json.loads(db.search(models.Posts, {"id": id}))[0])
        return render_template('make-post.html', form=form, edit=True)
        
        
    if __name__ == "__main__":
        app.run(debug=True)
    
    
create_app()