from wtforms import Form, TextAreaField, validators
from wtforms.validators import DataRequired

class AddEntryForm(Form):
    entry_text = TextAreaField('entry_text', [validators.InputRequired()])
