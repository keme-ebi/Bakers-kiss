"""
Application factory to help create multiple instances of the application
"""
from flask import Flask
from flask_restx import Api
from .orders.views import order
from .auth.views import auth
from .config.config import config_dict

def create_app(config=config_dict['dev']):
    """returns the application and hold configuration"""
    app = Flask(__name__)

    app.config.from_object(config)

    api = Api(app)

    api.add_namespace(order)
    api.add_namespace(auth, path='/auth')

    return app