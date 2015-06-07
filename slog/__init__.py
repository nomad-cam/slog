from flask import Flask
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

import slog.views
