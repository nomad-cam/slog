from flask import render_template,session,redirect,url_for,request,current_app,make_response

from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.sql import extract,and_,or_

from flask.ext.wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired

from slog import app
from config import data
from slog.models import ElogGroupData,ElogGroups,ElogData,SolUsers,SolUsersPrefsGroups,ElogKeywords,ElogKeywordData,ElogBeamModeData,ElogSeverityData
from slog.database import db

import ldap
from datetime import datetime
from avatar_generator import Avatar



# desired paths /<groupUrl>/<year>/<month>/<day>
@app.route('/')
def slog():
    return render_template('index.html')

class OptionsForm(Form):
    groups = ElogGroups.query.filter(ElogGroups.group_id,ElogGroups.elog_group_data)
    group_choices = [('1','Operators'),('2','IR'),('3','Far-IR')]
    page_choices = [('1','25'),('2','50'),('3','75'),('4','100'),('5','ALL')]
    nickname = StringField('Nickname:', validators=[DataRequired()])
    default_group = SelectField('Default Group:', choices=group_choices, validators=[DataRequired()])
    view_gropus = SelectMultipleField('View Groups:', choices=group_choices, validators=[DataRequired()])
    entries_per_page = SelectField('Entries per Page:', choices=page_choices, validators=[DataRequired()])
    # submit = SubmitField('Save Changes') #needed in footer of panel

@app.route('/options/', methods=['GET', 'POST'])
def options():
    form = OptionsForm()
    if form.validate_on_submit():
        pass
    return render_template('options.html', form=form)

#https://github.com/maethor/avatar-generator
@app.route('/avatar.png')
def avatar():
    try:
        initials = request.args.get('name')
        size = int(request.args.get('size'))
        colour = request.args.get('colour')
    except Exception:
        initials = "#"
        size = 128

    avatar = Avatar.generate(size=size, string=initials, filetype='PNG', colour=colour)
    headers = {'Content-Type': 'image/png'}
    return make_response(avatar, 200, headers)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404