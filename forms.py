from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField, DecimalField, RadioField
from wtforms.validators import DataRequired, URL

class NewCafeForm(FlaskForm):
    Cafename = StringField('Cafe name', validators=[DataRequired()])
    Location = StringField('Location', validators=[DataRequired()])
    Mapurl = StringField('Google Maps URL (If known)', validators=[DataRequired(), URL()])
    Imageurl = StringField('Image URL (If known)', validators=[DataRequired(), URL()])
    Socket = SelectField(label='Does the cafe have power sockets available?', choices=[("Yes"), ("No")], validators=[DataRequired()])
    Toilet = SelectField(label='Does the cafe have toilets available?', choices=[("Yes"), ("No")], validators=[DataRequired()])
    WiFi = SelectField(label='Does the cafe have free Wi-Fi available?', choices=[("Yes"), ("No")], validators=[DataRequired()])
    Calls = SelectField(label='Can you take calls in this cafe?', choices=[("Yes"), ("No")], validators=[DataRequired()])
    Seats = StringField('How many seats (estimated)?', validators=[DataRequired()])
    Price = StringField('How much for a standard cup of coffee?', validators=[DataRequired()])
    submit = SubmitField('Submit new Cafe')

class SearchForm(FlaskForm):
    Location = StringField('Location to search', validators=[DataRequired()])
    submit = SubmitField('Search for cafes...')
