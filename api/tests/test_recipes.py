import unittest
from flask_jwt_extended import create_access_token
from .. import create_app
from ..config.config import config_dict
from ..utils import db
from werkzeug.security import generate_password_hash
from ..models.user import User
from ..models.recipes import Recipe


class TestRecipes(unittest.TestCase):
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
            "pastry_name": "vanilla",
            "recipe": "...gram of sugar, ...gram of butter..."
        }


    def tearDown(self):
        db.drop_all()
        self.appctxt.pop()
        self.app = None
        self.client = None

    def test_get_all_recipes(self):
        response = self.client.get('/recipes/', headers=self.headers)

        assert response.status_code == 200

        assert response.json == []

    def test_create_new_recipe(self):
        response = self.client.post('/recipes/', json=self.data, headers=self.headers)

        assert response.status_code == 201

        recipe = Recipe.query.all()

        assert len(recipe) == 1

    def test_get_a_recipe(self):
        post = self.client.post('/recipes/', json=self.data, headers=self.headers)

        response = self.client.get('/recipes/1', headers=self.headers)

        assert response.status_code == 200

        user = User.query.filter_by(username='testuser').first()
        recipe = Recipe.query.filter_by(user=user,recipe_id=1).first()

        assert response.json == post.json

    def test_update_a_recipe(self):
        post = self.client.post('/recipes/', json=self.data, headers=self.headers)

        update = {
            "pastry_name": "sponge cake"
        }
        response = self.client.put('/recipes/1', json=update, headers=self.headers)

        assert response.status_code == 200

    def test_delete_a_recipe(self):
        post = self.client.post('/recipes/', json=self.data, headers=self.headers)

        response = self.client.delete('/recipes/1', headers=self.headers)

        assert response.status_code == 204

        recipe = Recipe.query.all()

        assert len(recipe) == 0