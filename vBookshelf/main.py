from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
import db


class EditForm(FlaskForm):
    rating = SelectField('Rating', validators=[DataRequired()], choices=[('⭐', '⭐'), ('⭐⭐', '⭐⭐'), ('⭐⭐⭐', '⭐⭐⭐'), ('⭐⭐⭐⭐', '⭐⭐⭐⭐'), ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')])
    submit = SubmitField(label='Change Rating')
    
    
class Form(FlaskForm):
    name = StringField('Book title', validators=[DataRequired()])
    author = StringField('Book author', validators=[DataRequired()])
    rating = SelectField('Rating', validators=[DataRequired()], choices=[('⭐', '⭐'), ('⭐⭐', '⭐⭐'), ('⭐⭐⭐', '⭐⭐⭐'), ('⭐⭐⭐⭐', '⭐⭐⭐⭐'), ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')])
    submit = SubmitField(label='Submit')


app = Flask(__name__)
Bootstrap(app)
app.config["SECRET_KEY"]="i made you read"


@app.route('/')
def home():
    all_books = [{'title':db.titles()[i], 'author':db.authors()[i], 'rating':db.ratings()[i]} for i in range(len(db.titles()))]
    return render_template('index.html', all_books=all_books)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = Form()
    if form.validate_on_submit():
        db.insert_row(form.name.data, form.author.data, form.rating.data)
        return redirect(url_for('home'))
    return render_template('add.html', form=form)


@app.route('/edit/<title>', methods=['GET', 'POST'])
def edit(title):
    form = EditForm()
    if form.validate_on_submit():
        db.change_rating(title, form.rating.data)
        return redirect(url_for('home'))
    return render_template('edit.html', form=form, title=title)


@app.route('/delete/<title>', methods=['GET', 'POST'])
def delete(title):
    db.delete_row(title)
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

    