from flask import render_template
from datetime import datetime
from app import app
from .forms import AddEntryForm
from flask import redirect

# Hello World Endpoint
@app.route('/hello')
def hello():
    return "Hello, Flask"

# render_template - Renders Template from template folder
@app.route('/')
def index():
    return render_template('index.html', user='Aayush')

@app.route('/entry/today', methods=['GET', 'POST'])
def add_entry():
    form = AddEntryForm()

    if form.validate_on_submit():
        print("Something got added")
        return redirect('/')
    today_date = datetime.now().date()
    return render_template('add_entry.html', today_date=today_date, form= form)