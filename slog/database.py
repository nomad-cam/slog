__author__ = 'roddac'


from slog import app
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
