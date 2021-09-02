# This files makes the website folder a python package. The init is the vital element to this.

from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy # Backend database
from os import path
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = "tmb_cv_2021"


def create_app():
    app = Flask(__name__, template_folder="templates")   # Initialise Flask
    app.config["SECRET_KEY"] = "yasv32trgweg"   # Encrypts cookies/session data
    #Tell flask where the database is stored
    app.config["SQLALCHEMY_DATBASE URI"] = f"sqlite:///{DB_NAME}" 
    db.init_app(app)    #Defines database into app

    from .views import views    # views.py - routes/endpoints
    from .auth import auth      # auth.py - routes/endpoints

    app.register_blueprint(views, url_prefix = "/")
    app.register_blueprint(auth, url_prefix = "/")

    from .models import User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    from .models import User
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        with app.app_context():
            u1 = User(username='admin', password='sha256$xD4J7yx6U6ZqnxXS$fac1b1f57d359836cd15adff34d69482c78176cb791d9e741a52365c96d37a59')
            u2 = User(username="butterworthcv", password='sha256$V1I4NWSUNC8Z03eS$10ba4f3ad28892211e0682ef595fcaba7da3d8bd6b39e62efeadc62409cff8ec')
            db.session.add(u1)
            db.session.add(u2)
            db.session.commit()
            print('Created Database!')