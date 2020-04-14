# this is card randomizer app
# all rights reserved DLX Design Lab

from flask import render_template, url_for
from app import app
from app import setBlueprint
import random

app.register_blueprint(setBlueprint.js)
app.register_blueprint(setBlueprint.css)
app.register_blueprint(setBlueprint.image)
randomize_cards_cache = []


################################################################################

# home page
@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

# character_cards page
@app.route('/cards01', methods=['GET', 'POST'])
def cards01():
    return render_template('cards01.html')

# context_cards page
@app.route('/cards02', methods=['GET', 'POST'])
def cards02():
    return render_template('cards02.html')

# parameter_cards page
@app.route('/cards03', methods=['GET', 'POST'])
def cards03():
    return render_template('cards03.html')


#################################################################################

# random number for character cards
@app.route('/randomNum_character_cards', methods=['GET'])
def randomize_number_character_cards():
    global randomize_cards_cache
    n = 13
    l = len(randomize_cards_cache)
    while l < n:
        r = random.randint(1,n)
        if r not in randomize_cards_cache:
            randomize_cards_cache.append(r)
            return str(r)
    else:
        randomize_cards_cache.clear()
        randomize_cards_cache.append(1)
        return str(1)

# random number for context cards
@app.route('/randomNum_context_cards', methods=['GET'])
def randomize_number_context_cards():
    global randomize_cards_cache
    n = 48
    l = len(randomize_cards_cache)
    while l < n:
        r = random.randint(1,n)
        if r not in randomize_cards_cache:
            randomize_cards_cache.append(r)
            return str(r)
    else:
        randomize_cards_cache.clear()
        randomize_cards_cache.append(1)
        return str(1)

# random number for parameter cards
@app.route('/randomNum_parameter_cards', methods=['GET'])
def randomize_number_parameter_cards():
    global randomize_cards_cache
    n = 18
    l = len(randomize_cards_cache)
    while l < n:
        r = random.randint(1,n)
        if r not in randomize_cards_cache:
            randomize_cards_cache.append(r)
            return str(r)
    else:
        randomize_cards_cache.clear()
        randomize_cards_cache.append(1)
        return str(1)