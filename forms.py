from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.validators import URL, InputRequired


class AddProjectForm(FlaskForm):
    title = StringField('Project title')
    description = TextAreaField('Project description')
    demo_url = StringField('Demo URL', validators=[URL(message='NOT A VALID URL!')])
    
class UserForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])