from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class SignUpForm(FlaskForm):
    username = StringField('User Name')
    password = PasswordField('Password')
    submit = SubmitField('Sign up')