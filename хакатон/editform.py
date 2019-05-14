from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired
 
 
class EditForm(FlaskForm):
    photo = URLField('URL for photo')
    status = TextAreaField('About')
    submit = SubmitField('Update')