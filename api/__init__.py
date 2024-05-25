"""
Application factory to help create multiple instances of the application
"""
from flask import Flask
from flask_restx import Api
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from .orders.views import orders
from .auth.views import auth
from .recipes.views import recipes
from .config.config import config_dict
from .utils import db
from .models.orders import Order
from .models.user import User
from .models.recipes import Recipe


def create_app(config=config_dict['dev']):
    """returns the application and hold configuration"""
    app = Flask(__name__)

    app.config.from_object(config)

    db.init_app(app)

    migrate = Migrate(app, db)

    api = Api(app)

    jwt = JWTManager(app)

    api.add_namespace(orders)
    api.add_namespace(recipes)
    api.add_namespace(auth, path='/auth')

    @app.shell_context_processor
    def make_shell_context():
        return {
            'db': db,
            'User': User,
            'Order': Order,
            'Recipe': Recipe
        }

    return app