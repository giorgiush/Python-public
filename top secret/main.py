from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap

class MyForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(3)])
    submit = SubmitField(label='Log in')


app = Flask(__name__)
Bootstrap(app=app)
app.secret_key = "I made you read"


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    login=MyForm()
    print(login.validate_on_submit())
    print(login.email.data)
    print(login.password.data)
    if login.validate_on_submit():
        if login.email.data == "top@secret.com" and login.password.data == "123":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login)


if __name__ == '__main__':
    app.run(debug=True)