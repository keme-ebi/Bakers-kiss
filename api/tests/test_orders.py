import unittest
from flask_jwt_extended import create_access_token
from .. import create_app
from ..config.config import config_dict
from ..utils import db
from werkzeug.security import generate_password_hash
from ..models.user import User
from ..models.orders import Order


class TestOrders(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config=config_dict['test'])
        self.appctxt = self.app.app_context()

        self.appctxt.push()
        self.client = self.app.test_client()
        db.create_all()

        mock_user = User(
            username='testuser',
            email='testuser@example.com',
            password=generate_password_hash('testpassword')
        )
        db.session.add(mock_user)
        db.session.commit()

        token = create_access_token(identity='testuser')

        self.headers = {
            "Authorization": f"Bearer {token}"
        }

        self.data = {
            "client": "testclient",
            "order_title": "testcake",
            "description": "a test cake of 3 layers",
            "price": 20.43,
            "due_date": "2024-05-29"
        }


    def tearDown(self):
        db.drop_all()
        self.appctxt.pop()
        self.app = None
        self.client = None

    def test_get_all_orders(self):
        response = self.client.get('/orders/', headers=self.headers)

        assert response.status_code == 200

        assert response.json == []

    def test_create_new_order(self):
        response = self.client.post('/orders/', json=self.data, headers=self.headers)

        assert response.status_code == 201

        orders = Order.query.all()

        assert len(orders) == 1

    def test_get_an_order(self):
        post = self.client.post('/orders/', json=self.data, headers=self.headers)

        response = self.client.get('/orders/1', headers=self.headers)

        assert response.status_code == 200

        user = User.query.filter_by(username='testuser').first()
        orders = Order.query.filter_by(user=user,order_id=1).first()

        assert response.json == post.json

    def test_update_an_order(self):
        post = self.client.post('/orders/', json=self.data, headers=self.headers)

        update = {
            "client": "tester"
        }
        response = self.client.put('/orders/1', json=update, headers=self.headers)

        assert response.status_code == 200

    def test_delete_an_order(self):
        post = self.client.post('/orders/', json=self.data, headers=self.headers)

        response = self.client.delete('/orders/1', headers=self.headers)

        assert response.status_code == 204

        orders = Order.query.all()

        assert len(orders) == 0