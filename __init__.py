from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_login import LoginManager

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config["DEBUG"] = True
    app.secret_key = 'changethiskey'

    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
        '''username="ADD USERNAME",
        password="ADD PASSWORD",
        hostname="ADD HOSTNAME",
        databasename="ADD DATABASE NAME",'''
        )

    app.config['SECRET_KEY'] = 'thissecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_POOL_RECYCLE'] = 280
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



    engine = create_engine(SQLALCHEMY_DATABASE_URI, convert_unicode=True, pool_recycle=280)
    db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))


    db.init_app(app)
    Base = declarative_base()
    Base.query = db_session.query_property()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from bandbucks import bb as bb_blueprint
    app.register_blueprint(bb_blueprint)



    return app









