"""
Application factory to help create multiple instances of the application
"""
from flask import Flask
from flask_restx import Api
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from werkzeug.exceptions import NotFound, MethodNotAllowed
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

    # configuration of flask app
    app.config.from_object(config)

    # database initialization
    db.init_app(app)

    migrate = Migrate(app, db)

    authorizations = {
        "Bearer Auth": {
            "type": "apiKey",
            "in" : "header",
            "name": "Authorization",
            "description": "Add a JWT with **Bearer &lt;JWT&gt;** to authorize"
        }
    }

    # flask_restx api instance
    api = Api(
        app,
        title="Bakers-kiss API",
        description="A REST API for bakers to keep track of their orders, store recipes and get reminders on when to restock",
        authorizations=authorizations,
        security="Bearer Auth"
    )

    # flask-jwt instance
    jwt = JWTManager(app)

    # flask_restx routes/namespaces
    api.add_namespace(orders)
    api.add_namespace(recipes)
    api.add_namespace(auth, path='/auth')

    # flask-mail initialization
    mail = Mail(app)

    # for creation of database using "flask shell" command
    @api.errorhandler(NotFound)
    def not_found(error):
        return {"error": "Ololololo"}, 404

    @api.errorhandler(MethodNotAllowed)
    def method_not_allowed(error):
        return {"error": "method not allowed"}, 405

    @app.shell_context_processor
    def make_shell_context():
        return {
            'db': db,
            'User': User,
            'Order': Order,
            'Recipe': Recipe
        }

    # attach mail instance to the Flask application instance
    app.mail = mail

    return app