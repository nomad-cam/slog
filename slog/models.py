from slog.database import db
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class ElogGroupData(db.Model):

    __tablename__ = 'elog_group_data'

    group_id = db.Column(db.Integer, primary_key=True)
    group_title = db.Column(db.Text)
    sort = db.Column(db.Integer)
    private = db.Column(db.Integer)
    urlName = db.Column(db.Text)


class ElogGroups(db.Model):
    __tablename__ = 'elog_groups'

    entry_id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, primary_key=True)

    elog_group_data_id = db.Column(db.Integer, db.ForeignKey('elog_group_data.group_id'))
    elog_group_data = db.relationship('ElogGroupData')


class ElogData(db.Model):

    __tablename__ = 'elog_data'

#   entry_id    title   author  created text    severity_id beam_mode_id    parent_id   read_only   comment
    entry_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    author = db.Column(db.Text)
    created = db.Column(db.DateTime)
    text = db.Column(db.Text)
    severity_id = db.Column(db.Integer)
    beam_mode_id = db.Column(db.Integer)
    parent_id = db.Column(db.Integer)
    read_only = db.Column(db.Integer)
    comment = db.Column(db.Integer)


class SolUsers(db.Model):

    __tablename__ = 'sol_users'

#	id	name	username	email	password	usertype	gid	registerDate	lastvisitDate	elog_hide_important //
#   elog_collapse_all	elog_entries_per_page	site_nickname	elog_simple_editor	elog_shadow_boxer //
#   elog_show_keywords	elog_date_format	guest
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(255))
    username = db.Column(db.VARCHAR(150))
    email = db.Column(db.VARCHAR(100))
    password = db.Column(db.VARCHAR(100))
    usertype = db.Column(db.VARCHAR(25))
    gid = db.Column(db.Integer)
    registerDate = db.Column(db.DateTime)
    lastvisitDate = db.Column(db.DateTime)
    elog_hide_important = db.Column(db.Integer)
    elog_collapse_all = db.Column(db.Integer)
    elog_entries_per_page = db.Column(db.Integer)
    site_nickname = db.Column(db.VARCHAR(255))
    elog_simple_editor = db.Column(db.Integer)
    elog_shadow_boxer = db.Column(db.Integer)
    elog_show_keywords = db.Column(db.Integer)
    elog_date_format = db.Column(db.Text)
    guest = db.Column(db.Integer)


class SolUsersPrefsGroups(db.Model):

    __tablename__ = 'sol_users_prefs_groups'

#    	user_id	group_id
    user_id = db.Column(db.Integer,primary_key=True)
    group_id = db.Column(db.Integer,primary_key=True)


class ElogKeywords(db.Model):

    __tablename__ = 'elog_keywords'

#	entry_id	keyword_id
    entry_id = db.Column(db.Integer, primary_key=True)
    keyword_id = db.Column(db.Integer,primary_key=True)


class ElogKeywordData(db.Model):

    __tablename__ = 'elog_keyword_data'

#	keyword_id	keyword_title	sort
    keyword_id = db.Column(db.Integer, primary_key=True)
    keyword_title = db.column(db.VARCHAR(32))
    sort = db.Column(db.Integer)


class ElogBeamModeData(db.Model):

    __tablename__ = 'elog_beam_mode_data'

#	beam_mode_id	beam_mode_title
    beam_mode_id = db.Column(db.Integer,primary_key=True)
    beam_mode_title = db.Column(db.VARCHAR(32))


class ElogSeverityData(db.Model):

    __tablename__ = 'elog_severity_data'

#	severity_id	      severity_title	severity_icon
    severity_id = db.Column(db.Integer,primary_key=True)
    severity_title = db.Column(db.VARCHAR(32))
    severity_icon = db.Column(db.VARCHAR(32))

