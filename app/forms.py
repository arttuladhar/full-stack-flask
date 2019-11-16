from flask_wtf import Form
from wtforms import StringField, TextAreaField, validators
from wtforms.validators import DataRequired

class AddEntryForm(Form):
    entry_text = TextAreaField('entry_text', validators=[DataRequired()])

