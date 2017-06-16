from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.plugins import Plugin
from flask import current_app as app
from .views import blueprint

__plugin__ = "Quiz"

#app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

class Quiz(Plugin):
    def setup(self):
        app.register_blueprint(blueprint, url_prefix="/user_evaluation")

from app import views, questions
