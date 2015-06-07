from flask import render_template,session,redirect,url_for,request,current_app

from slog import app

from datetime import datetime


@app.route('/')
def slog():
    return render_template("index.html")
