from flask import Flask
from flask_cors import CORS
from database import db
from queue import Queue
import os

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = f"{os.environ.get('DB_URL')}?ssl_ca=ca-certificate.crt"

    db.init_app(app)

    with app.app_context():
        db.create_all()


    from endpoints.api import api

    app.register_blueprint(api)

    return app
