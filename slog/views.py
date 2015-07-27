from flask import render_template,session,redirect,url_for,request,current_app

from slog import app
from config import data
from slog.models import ElogGroupData,ElogGroups,ElogData,SolUsers
from slog.database import db

from sqlalchemy.sql import extract,and_,or_
import ldap
from datetime import datetime


# desired paths /<groupUrl>/<year>/<month>/<day>
@app.route('/')
def slog():
    return render_template("index.html")

@app.route('/options/')
def options():
    return render_template("options.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404