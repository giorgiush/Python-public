from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
from flask_bootstrap import Bootstrap
import pandas as pd

class MyForm(FlaskForm):
    name = StringField('Cafe Name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps (URL)', validators=[URL()])
    open = StringField('Opening Time', validators=[DataRequired()])
    close = StringField('Closing Time', validators=[DataRequired()])
    coffee = SelectField('Coffee Rating', validators=[DataRequired()], choices=[('☕️', '☕️'), ('☕️☕️', '☕️☕️'), ('☕️☕️☕️', '☕️☕️☕️'), ('☕️☕️☕️☕️', '☕️☕️☕️☕️'), ('☕️☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'),])
    wifi = SelectField('Wifi Strength', validators=[DataRequired()], choices=[('✘', '✘'), ('💪', '💪'), ('💪💪', '💪💪'), ('💪💪💪', '💪💪💪'), ('💪💪💪💪', '💪💪💪💪'), ('💪💪💪💪💪', '💪💪💪💪💪'),])
    power = SelectField('Power Socket Availability', validators=[DataRequired()], choices=[('🔌', '🔌'), ('🔌🔌', '🔌🔌'), ('🔌🔌🔌', '🔌🔌🔌'), ('🔌🔌🔌🔌', '🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌🔌'),])
    submit = SubmitField(label='Submit')
    
    
app = Flask(__name__)
Bootstrap(app)
app.secret_key = "I made you read"


@app.route('/')
def homepage():
    return render_template("index.html")



@app.route('/cafes')
def cafes():
    
    data = pd.read_csv('day_62_coffee_and_wifi/data.csv')
    columns = data.columns
    
    cafes = []
    for index, row in data.iterrows():
        temp_list = []
        for column in columns:
            temp_list.append(row[f"{column}"])
        cafes.append(temp_list)

    return render_template("cafes.html", columns=columns, cafes=cafes)
    
    
    
@app.route('/add', methods=['GET', 'POST'])
def add():
    
    form = MyForm()
    
    if form.validate_on_submit():
        data = pd.read_csv('day_62_coffee_and_wifi/data.csv')
        new_data = pd.DataFrame({'Cafe Name': [f'{form.name.data}'],
                            'Location': [f'{form.location.data}'],
                            'Open': [f'{form.open.data}'],
                            'Close': [f'{form.close.data}'],
                            'Coffee': [f'{form.coffee.data}'],
                            'Wifi': [f'{form.wifi.data}'],
                            'Power': [f'{form.power.data}']}) 
        data = pd.concat([data, new_data], ignore_index=True)
        data.to_csv('day_62_coffee_and_wifi/data.csv', index=False)
        return redirect(url_for('cafes'))
    
    return render_template("forms.html", form=form)
    
    
    
if  __name__ == "__main__":
    app.run(debug=True)


