from wtforms import Form, StringField, TextAreaField, validators
from wtforms.validators import DataRequired

class AddEntryForm(Form):
    entry_mood = StringField('mood', validators=[DataRequired])
    entry_text = TextAreaField('entry_text')

