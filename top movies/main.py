from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
import db
import moviefinder


class MovieTitle(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField(label='Add Movie')
    
class EditMovie(FlaskForm):
    rating = StringField('Your Rating', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField(label='Update')    
    
    
app = Flask(__name__)
Bootstrap(app)
app.secret_key = "I made you read"



def create_app():
    @app.route('/')
    def home():
        print(db.get_list_length())
        return render_template('index.html', movies=db.get_movies(), list_length = db.get_list_length())  
    
    @app.route('/add', methods=['GET', 'POST'])
    def add():
        form = MovieTitle()
        if form.validate_on_submit():
            return redirect(url_for('select', title=form.title.data))
        return render_template('add.html', form=form)
        
    @app.route('/edit/<title>/<year>', methods=['GET', 'POST'])
    def edit(title, year):
        form = EditMovie()
        if form.validate_on_submit():
            db.change_data(title=title, year=year, rating=form.rating.data, review=form.review.data)
            return redirect(url_for('home'))
        return render_template('edit.html', form=form, title=title)
    
    @app.route('/delete/<title>/<year>', methods=['GET', 'POST'])
    def delete(title, year):
        db.delete_movie(title, year)
        return redirect(url_for('home'))
    
    @app.route('/select/<title>', methods=['GET', 'POST'])
    def select(title):
        return render_template('select.html', movies=moviefinder.find_movie(title))
    
    @app.route('/update/<int:id>', methods=['GET', 'POST'])
    def update(id):
        movie_data = moviefinder.selected_movie_data(id)
        db.add_movie(title=movie_data['title'], year=movie_data['year'], description=movie_data['description'], image=movie_data['image'], review="", rating="")
        return redirect(url_for('edit', title=movie_data['title'], year=movie_data['year']))
    
    if __name__ == "__main__":
        app.run(debug=True)
    
create_app()
