from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField
from wtforms.validators import DataRequired, Length, NumberRange

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    account_number = StringField('Account Number', validators=[DataRequired()])
    account_holder_name = StringField('Account Holder Name', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    mobile_number = StringField('Mobile Number', validators=[DataRequired()])
    balance = DecimalField('Initial Balance', validators=[DataRequired(), NumberRange(min=0)])
    card_number = StringField('Card Number', validators=[DataRequired()])
    card_holder_name = StringField('Card Holder Name', validators=[DataRequired()])
    expiration_date = StringField('Expiration Date', validators=[DataRequired()])
    cvv = StringField('CVV', validators=[DataRequired(), Length(min=3, max=4)])
    card_type = StringField('Card Type', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
