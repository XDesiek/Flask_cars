
import os

from flask import Flask
# from flask_bootstrap import Bootstrap
from flask_bootstrap import Bootstrap5
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
basedir = os.path.abspath(os.path.dirname(__file__))
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USERNAME'] = 'testflask8@gmail.com'
    app.config['MAIL_PASSWORD'] = 'aoil nuek myvn nnuc'
    app.config['MAIL_USE_TLS'] = True

    db.init_app(app)
    mail = Mail(app)
    migrate.init_app(app, db)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app


