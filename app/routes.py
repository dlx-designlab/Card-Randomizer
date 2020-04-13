# this is card randomizer app
# all rights reserved DLX Design Lab

from flask import render_template, url_for
from app import app
from app import setBlueprint
import random

app.register_blueprint(setBlueprint.js)
app.register_blueprint(setBlueprint.css)
app.register_blueprint(setBlueprint.image)
randomize_cards_cache=[]

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/randomcards', methods=['GET'])
def randomize():
    global randomize_cards_cache
    randomNum = random.randint(1,13)
    return str(randomNum)