from flask import render_template, jsonify, redirect
from datetime import datetime

from flask.globals import request
from app import app

from .forms import AddEntryForm
from .extensions import db
from .models import User, Entry

@app.cli.command("initdb")
def initdb():

    # Creating Seed Data
    for num in range(10):
        db.session.add(User(username='Flask' + str(num), email='flask' + str(num) + '@gmail.com'))
        db.session.commit()

    db.session.add(Entry(text='Hello World'))
    db.session.commit()

    db.create_all()
    print ("Created Tables")

# Hello World Endpoint
@app.route('/hello')
def hello():
    return "Hello, Flask"

# render_template - Renders Template from template folder
@app.route('/')
def index():
    entries = []
    entries = Entry.query.all()
    print(entries)
    return render_template('index.html', user='Aayush', entries=entries)

@app.route('/users')
def get_users():
    resp_user = []
    users = User.query.all()
    return jsonify ( list(map(lambda user: user.serialize(), users)) )

@app.route('/entry/today', methods=['GET', 'POST'])
def add_entry():

    form = AddEntryForm(request.form)
    if request.method == 'POST' and form.validate():        
        print("Something got added: " + form.entry_text.data)
        db.session.add(Entry(text=form.entry_text.data))
        db.session.commit()
        return redirect('/')

    today_date = datetime.now().date()
    return render_template('add_entry.html', today_date=today_date, form=form)