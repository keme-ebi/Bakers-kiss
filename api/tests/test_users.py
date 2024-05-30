import unittest
from .. import create_app
from ..config.config import config_dict
from ..utils import db
from werkzeug.security import generate_password_hash
from ..models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        """s"""
        self.app = create_app(config=config_dict['test'])
        self.appctxt = self.app.app_context()

        self.appctxt.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        """d"""
        db.drop_all()
        self.appctxt.pop()
        self.app = None
        self.client = None

    def test_user_signup(self):
        """tests new users"""
        data = {
            "username": "testuser",
            "email": "testuser@mail.com",
            "password": "testpassword"
        }
        response = self.client.post('/auth/signup', json=data)

        user = User.query.filter_by(email=data['email']).first()

        assert user.username == data['username']

        assert response.status_code == 201

    def test_user_signup_with_missing_username(self):
        data = {
            "username": "",
            "email": "testuser@mail.com",
            "password": "testpassword"
        }

        response = self.client.post('/auth/signup', json=data)

        assert response.status_code == 409

    def test_user_signup_with_missing_email(self):
        data = {
            "username": "testuser",
            "email": "",
            "password": "testpassword"
        }

        response = self.client.post('/auth/signup', json=data)

        assert response.status_code == 409

    def test_user_signup_with_missing_password(self):
        data = {
            "username": "testuser",
            "email": "testuser@mail.com",
            "password": ""
        }

        response = self.client.post('/auth/signup', json=data)

        assert response.status_code == 400

    def test_user_login_for_existing_user(self):
        data = {
            "username": "testuser",
            "email": "testuser@mail.com",
            "password": "testpassword"
        }
        signup_response = self.client.post('/auth/signup', json=data)

        login_data = {
            "email": "testuser@mail.com",
            "password": "testpassword"
        }

        login_response = self.client.post('/auth/login', json=login_data)
        
        assert login_response.status_code == 200

    def test_user_login_for_non_existing_user(self):
        data = {
            "email": "testuser@mail.com",
            "password": "testpassword"
        }
        response = self.client.post('/auth/login', json=data)

        assert response.status_code == 400

    def test_user_login_for_no_email(self):
        data = {
            "email": "",
            "password": "testpassword"
        }
        response = self.client.post('/auth/login', json=data)

        assert response.status_code == 400

    def test_user_login_for_no_password(self):
        data = {
            "email": "testuser@mail.com",
            "password": ""
        }
        response = self.client.post('/auth/login', json=data)

        assert response.status_code == 400