from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, TextAreaField

class SignUpForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    email = StringField('email')
    message = TextAreaField('Message')
    is_recruiter = RadioField('Are you a recruiter?', choices=['Yes', 'No'])
    submit = SubmitField('Click to send this message to Victor')