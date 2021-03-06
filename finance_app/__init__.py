from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# from flask_login import LoginManager
from flask_mail import Mail
from finance_app.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
# login_manager = LoginManager()
# login_manager.login_view = 'users.login'
# login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)
    # login_manager.init_app(app)
    mail.init_app(app)

    # This needs to imported after creating the app to prevent circular imports
    from finance_app.main.routes import main  # main is the blueprint variable
    from finance_app.errors.handlers import errors

    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
