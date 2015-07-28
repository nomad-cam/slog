from flask import render_template,session,redirect,url_for,request,current_app,make_response

from slog import app
from config import data
from slog.models import ElogGroupData,ElogGroups,ElogData,SolUsers
from slog.database import db

from sqlalchemy.sql import extract,and_,or_
import ldap
from datetime import datetime
from avatar_generator import Avatar


# desired paths /<groupUrl>/<year>/<month>/<day>
@app.route('/')
def slog():
    return render_template('index.html')

@app.route('/options/')
def options():
    return render_template('options.html')

#https://github.com/maethor/avatar-generator
@app.route('/avatar.png')
def avatar():
    try:
        initials = request.args.get('name')
        size = int(request.args.get('size'))
    except Exception:
        initials = "#"
        size = 128

    avatar = Avatar.generate(size=size, string=initials, filetype='PNG')
    headers = {'Content-Type': 'image/png'}
    return make_response(avatar, 200, headers)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404