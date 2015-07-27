from flask import render_template,session,redirect,url_for,request,current_app

from slog import app
from config import data
from slog.models import ElogGroupData,ElogGroups,ElogData,SolUsers
from slog.database import db

from sqlalchemy.sql import extract,and_,or_
import ldap
from datetime import datetime


@app.route('/')
def slog():
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404