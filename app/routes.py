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
    db.session.add(User(username='Flask', email='flask@gmail.com'))
    db.session.add(Entry(text='Hello World'))
    db.session.commit()
    
    db.create_all()
    print ("Tables Created")

@app.cli.command("dropdb")
def initdb():    
    db.drop_all()
    print ("Tables Deleted")

# Hello World Endpoint
@app.route('/hello')
def hello():
    return "Hello, Flask"

# render_template - Renders Template from template folder
@app.route('/')
def index():
    try:
        entries = []
        entries = Entry.query.all()
        print(entries)
        return render_template('index.html', user='Aayush', entries=entries)
    except Exception as e:
        print(e)

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
        try:
            db.session.add(Entry(text=form.entry_text.data))
            db.session.commit()
        except Exception as e:
            print ("Error: " + e)        
        return redirect('/')

    today_date = datetime.now().date()
    return render_template('add_entry.html', today_date=today_date, form=form)