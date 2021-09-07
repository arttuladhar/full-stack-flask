from flask import render_template, jsonify, redirect
from datetime import datetime
from app import app

from .forms import AddEntryForm
from .extensions import db
from .models import User

@app.cli.command("initdb")
def initdb():

    # Creating Seed Data
    for num in range(10):
        db.session.add(User(username='Flask' + str(num), email='flask' + str(num) + '@gmail.com'))
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
    return render_template('index.html', user='Aayush')

@app.route('/users')
def get_users():
    resp_user = []
    users = User.query.all()

    return jsonify ( list(map(lambda user: user.serialize(), users)) )

@app.route('/entry/today', methods=['GET', 'POST'])
def add_entry():
    form = AddEntryForm()

    if form.validate_on_submit():
        print("Something got added")
        return redirect('/')
    today_date = datetime.now().date()
    return render_template('add_entry.html', today_date=today_date, form= form)