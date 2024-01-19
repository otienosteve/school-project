import datetime
import os 

from dotenv import load_dotenv
from flask import Flask 
from flask_migrate import Migrate
from flask_cors import CORS

from models import db
from course import course_bp
from main import main_bp
from auth import jwt, bcrypt, auth_bp


def create_app():

    load_dotenv()
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']= os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['JWT_ACCESS_TOKEN_EXPIRES']= datetime.timedelta(hours=1)
    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    migrate = Migrate(app, db)
    app.register_blueprint(course_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    CORS(app, resources={r"*": {"origins": "*"}})


    return app


app = create_app()