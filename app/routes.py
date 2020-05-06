# this is card randomizer app
# all rights reserved DLX Design Lab

from flask import render_template, url_for, redirect #templates
from flask import render_template, flash, redirect #login form
from flask import request, make_response #cookies

from app import app, db
from app.forms import LoginForm, RegistrationForm, AdminLoginForm, ResetPassForm
from app import setBlueprint

from flask_login import current_user, login_user, login_required #login_admin
from app.models import Pass, User 
from werkzeug.urls import url_parse

import random
import os
import sys
import datetime
import glob
import json

app.register_blueprint(setBlueprint.js)
app.register_blueprint(setBlueprint.css)
app.register_blueprint(setBlueprint.image)

# global
cache_01 = []
cache_02 = []
cache_03 = []
cache_04 = []
counter_01 = str()
counter_02 = str()
counter_03 = str()
counter_04 = str()
with open('app/settings.json') as f:
    app_settings = json.load(f)
    
################################################################################

@app.route('/test', methods=['GET', 'POST'])
def test():
    return render_template('base_test.html')

# home page
@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    #login restriction with cookie
    status = request.cookies.get('status')
    if status == 'logged_in':
        return render_template('home.html')
    else:
        return redirect(url_for('login'))

# admin_register page
@app.route('/admin_register', methods=['GET', 'POST'])
def admin_register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered admin!')
        return redirect(url_for('admin_login'))
    return render_template('admin_register.html', title='Admin Register', form=form)

# Admin_login page
@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if current_user.is_authenticated:
        return redirect(url_for('admin'))
    form = AdminLoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('admin_login'))
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('admin')
        return redirect(next_page)
    return render_template('admin_login.html', title='Admin Sign In', form=form)

# admin page
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    form = ResetPassForm()
    if form.validate_on_submit():
#        pass = Pass()
#        pass.set_password(form.password.data)
#        db.session.commit()
        flash('the pass has been changed successfully!')
    return render_template('admin.html', title='Reset Pass', form=form)

# login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    #login with cookie
    status = request.cookies.get('status')
    if status == 'logged_in':
        return redirect(url_for('home')) 
    form = LoginForm()
    if form.validate_on_submit():
        if form.password.data == app_settings['password']:
            res = make_response(redirect(url_for('home')))
            res.set_cookie(
                'status',
                value = 'logged_in',
                max_age = None,
                expires = datetime.datetime.now() + datetime.timedelta(days=1),
                path = '/',
                domain = None,
                secure = False,
                )
            return res
        else:
            flash('wrong password')
    return render_template('login.html', title='Sign In', form=form)

##################################################################################

### character_cards page
@app.route('/cards_home/<card_type>')
def cards_home(card_type):
    #login restriction with cookie
    status = request.cookies.get('status')
    if status == 'logged_in':
        switcher={
            1:'character_cards',
            2:'context_cards',
            3:'parameter_cards',
            4:'rammojammo_cards',
        }
        cards_folder = switcher.get(int(card_type),"Invalid Card Type")
        return render_template('cards_home.html', cards_folder = cards_folder)
    else:
        return redirect(url_for('login'))

@app.route('/cards_deal/<cards_folder>', methods=['GET', 'POST'])
def cards_deal(cards_folder):
    list = os.listdir('app/static/image/' + cards_folder)
    cardsNum = len(list) - 1 
    return render_template('cards_deal.html', cards_folder = cards_folder, cardsNum = cardsNum)