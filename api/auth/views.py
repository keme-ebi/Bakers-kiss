from flask import request, current_app
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token,  create_refresh_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import Conflict, BadRequest
from flask_mail import Message
from http import HTTPStatus
from ..models.user import User


auth = Namespace('auth', description="authentication namespace")

signup_model = auth.model(
    'SignUp', {
        'id': fields.Integer(),
        'username': fields.String(required=True, description="a username for the user"),
        'email': fields.String(required=True, description="user's email"),
        'password': fields.String(required=True, description="user's password")
    }
)

user_model = auth.model(
    'User', {
        'id': fields.Integer(),
        'username': fields.String(required=True, description="a username for the user"),
        'email': fields.String(required=True, description="user's email"),
        'password': fields.String(required=True, description="user's password"),
        'created_at': fields.DateTime(readonly=True, description="the date user got created"),
        'updated_at': fields.DateTime(readonly=True, description="user updated")
    }
)

login_model = auth.model(
    'Login', {
        'email': fields.String(required=True, description="user's email"),
        'password': fields.String(required=True, description="user's password")
    }
)

@auth.route('/signup')
class SignUp(Resource):
    @auth.expect(signup_model)
    @auth.marshal_with(user_model)
    def post(self):
        """
        Signs up/Creates a new user
        """
        data = request.get_json()

        try:
            new_user = User(
                username = data.get('username'),
                email = data.get('email'),
                password = generate_password_hash(data.get('password'))
            )

            new_user.save()

            recipient = [data.get('email')]

            msg = Message(
                "Bakers-kiss Account Creation",
                recipients=recipient
            )
            msg.body = f"Congratulations, your account has been created successfully with username:{data.get('username')}, and email:{data.get('email')}"

            current_app.mail.send(msg)
            return new_user, HTTPStatus.CREATED
        except Exception as e:
            raise Conflict("Email already exists")

@auth.route('/login')
class Login(Resource):
    @auth.expect(login_model)
    def post(self):
        """
        Logs in user using JWT pair
        """
        data = request.get_json()

        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            acces_token = create_access_token(identity=user.username)
            refresh_token = create_refresh_token(identity=user.username)

            response = {
                'access_token': acces_token,
                'refresh_token': refresh_token
            }

            return response, HTTPStatus.OK

        raise BadRequest("Invalid email or password")


# This route can only be accessed if the user is authenticated
@auth.route('/refresh')
class RefreshToken(Resource):
    @jwt_required(refresh=True)
    def post(self):
        """
        Gets a new token when the original token expires
        """
        username = get_jwt_identity()

        access_token = create_access_token(identity=username)

        return {'access_token': access_token}, HTTPStatus.OK