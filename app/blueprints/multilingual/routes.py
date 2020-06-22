# this is card randomizer app
# all rights reserved DLX Design Lab

from flask import render_template, url_for, redirect, Blueprint, g, current_app, abort ### for templates
from flask import render_template, flash, redirect ### for login form
from flask import request, make_response ### for cookies
from flask_babel import _, refresh
from app import app
from app import setBlueprint

multilingual = Blueprint('multilingual', __name__, template_folder='templates', url_prefix='/<lang_code>')

@multilingual.url_defaults
def add_language_code(endpoint, values):
    values.setdefault('lang_code', g.lang_code)

@multilingual.url_value_preprocessor
def pull_lang_code(endpoint, values):
    g.lang_code = values.pop('lang_code')

@multilingual.before_request
def before_request():
    if g.lang_code not in current_app.config['LANGUAGES']:
        abort(404)


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

# admin page
@multilingual.route('/admin', methods=['GET', 'POST'])
def admin():
    psw_crt = request.form.get('psw_crt')
    psw_new = request.form.get('psw_new')
    if request.method == 'POST':
        if psw_crt == app_settings['password']:
            app_settings['password'] = psw_new
            with open('app/settings.json', 'w') as f:
                json.dump(app_settings, f)
                f.close()
            flash('Passcode Changed', 'success')
        else:
            flash('Wrong Password', 'error')
    return render_template('multilingual/admin.html')

# home page
@multilingual.route('/')
@multilingual.route('/home', methods=['GET', 'POST'])
def home():
    #login restriction with cookie
    status = request.cookies.get('status')
    if status == 'logged_in':
        return render_template('multilingual/home.html')
    else:
        return redirect(url_for('multilingual.login'))

# login page
@multilingual.route('/login', methods=['GET', 'POST'])
def login():
    #login with cookie
    status = request.cookies.get('status')
    if status == 'logged_in':
        return redirect(url_for('multilingual.home')) 
    psw = request.form.get('psw')
    if request.method == 'POST':
        if psw == app_settings['password_admin']:
            resp = make_response(render_template('multilingual/home.html'))
            resp.set_cookie(
                'status',
                value = 'logged_in',
                max_age = None,
                expires = None,
                path = '/',
                domain = None,
                secure = False,
                )
            resp.set_cookie(
                'admin_status',
                value = 'admin_logged_in',
                max_age = None,
                expires = None,
                path = '/',
                domain = None,
                secure = False,
                )
            return resp
        elif psw == app_settings['password_dlx']:
            resp2 = make_response(render_template('multilingual/home.html'))
            resp2.set_cookie(
                'status',
                value = 'logged_in',
                max_age = None,
                expires = None,
                path = '/',
                domain = None,
                secure = False,
                )
            return resp2
        if psw == app_settings['password']:
            resp3 = make_response(render_template('multilingual/home.html'))
            resp3.set_cookie(
                'status',
                value = 'logged_in',
                max_age = None,
                expires = datetime.datetime.now() + datetime.timedelta(days=1),
                path = '/',
                domain = None,
                secure = False,
                )
            return resp3
        else:
            flash('Wrong Password', 'error')
    return render_template('multilingual/login.html')

##################################################################################

@multilingual.route('/cards_home/<card_type>')
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
        
        #creat title for each card's home page e.g. character card
        rabel_list = cards_folder.split('_') 
        card_name = rabel_list[0] + ' card'
        
        return render_template('multilingual/cards_home.html', cards_folder = cards_folder, card_name = card_name)
    else:
        return redirect(url_for('multilingual.login'))

@multilingual.route('/cards_deal/<cards_folder>', methods=['GET', 'POST'])
def cards_deal(cards_folder):
    files_list = []
    #login restriction with cookie
    status = request.cookies.get('status')
    if status == 'logged_in':
        for file in os.listdir('app/static/image/' + cards_folder):
            if file.endswith(".jpg"):
                files_list.append(file)
        cardsNum = len(files_list) - 1 
        return render_template('multilingual/cards_deal.html', cards_folder = cards_folder, cardsNum = cardsNum)
    else:
        return redirect(url_for('multilingual.login'))