# this is card randomizer app
# all rights reserved DLX Design Lab

from flask import render_template, url_for, redirect #templates
from flask import render_template, flash, redirect #login form
from flask import request, make_response #cookies

from app import app, db
from app.forms import LoginForm, RegistrationForm
from app import setBlueprint

from flask_login import current_user, login_user, login_required #login_admin
from app.models import User 
from werkzeug.urls import url_parse

import random
import os
import sys
import datetime

app.register_blueprint(setBlueprint.js)
app.register_blueprint(setBlueprint.css)
app.register_blueprint(setBlueprint.image)
randomize_cards_cache = []


################################################################################

# home page
@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    return render_template('home.html', title='Home Page')

#    status = request.cookies.get('status')
#    if status == 'logged_in':
#        return render_template('home.html')
#    else:
#        return redirect(url_for('login'))

# register page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

# login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

#cookieを利用したログイン方法
#    form = LoginForm()
#    if form.validate_on_submit():
#        if form.password.data == 'xxx':
#            res = make_response(redirect(url_for('home')))
#            res.set_cookie(
#                'status',
#                value = 'logged_in',
#                max_age = None,
#                expires = datetime.datetime.now() + datetime.timedelta(days=90),
#                path = '/',
#                domain = None,
#                secure = False,
#                )
#            return res
#        else:
#            flash('wrong password')
#    return render_template('login.html', title='Sign In', form=form)


# character_cards page
@app.route('/cards01', methods=['GET', 'POST'])
@login_required
def cards01():
    return render_template('cards01.html')

# context_cards page
@app.route('/cards02', methods=['GET', 'POST'])
@login_required
def cards02():
    return render_template('cards02.html')

# parameter_cards page
@app.route('/cards03', methods=['GET', 'POST'])
@login_required
def cards03():
    return render_template('cards03.html')

# rammojammo_cards page
@app.route('/cards04', methods=['GET', 'POST'])
@login_required
def cards04():
    return render_template('cards04.html')

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

# random number for rammojammo cards
@app.route('/randomNum_rammojammo_cards', methods=['GET'])
def randomize_number_rammojammo_cards():
    global randomize_cards_cache
    n = 5
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




# cookies
@app.route('/cookies')
def cookies():

    #レスポンスオブジェクトを生成する
    res = make_response('Cookies', 200)
    
    #Cookieの設定を行う
    res.set_cookie(
        'status',
        value = 'logged_in',
        max_age = 30,
        expires = None,
        path = request.path,
        )
    
    #レスポンスオブジェクトを返す
    return res




    #cookie（辞書型）を取得し、key:'status'に対応するvalueを取り出す
    #status = request.cookies.get('status', None)
