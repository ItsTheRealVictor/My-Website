from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField
from wtforms.validators import URL


class AddProjectForm(FlaskForm):
    title = StringField('Project title')
    description = TextAreaField('Project description')
    demo_url = StringField('Demo URL', validators=[URL(message='NOT A VALID URL!')])