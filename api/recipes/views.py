from flask import request
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from http import HTTPStatus
from ..models.recipes import Recipe
from ..models.user import User
from ..utils import db

recipes = Namespace('recipes', description="recipes namespace")

recipe_model = recipes.model(
    'Recipes', {
        'recipe_id': fields.Integer(description="id of the recipe"),
        'pastry_name': fields.String(required=True, description="the name of pastry"),
        'recipe': fields.String(required=True, description="instructions on how to make the pastry"),
        'created_at': fields.DateTime(readonly=True, description="date recipe was entered"),
        'updated_at': fields.DateTime(readonly=True, description="date recipe got updated")
    }
)

input_recipe = recipes.model(
    'NewRecipe', {
        'pastry_name': fields.String(required=True, description="the name of the pastry"),
        'recipe': fields.String(required=True, description="instructions on how to make the pastry")
    }
)

@recipes.route('/')
class Recipes(Resource):
    @recipes.marshal_with(recipe_model)
    @recipes.doc(
        description="Retrieves all recipes of an authorized user"
    )
    @jwt_required()
    def get(self):
        """
        Display all recipes of the user only
        """
        username = get_jwt_identity()

        current_user = User.query.filter_by(username=username).first()

        if not current_user:
            return {'message': 'User not found'}, HTTPStatus.NOT_FOUND

        orders = Recipe.query.filter_by(user=current_user).all()

        return orders, HTTPStatus.OK

    @recipes.marshal_with(recipe_model)
    @recipes.expect(input_recipe)
    @recipes.doc(
        description="Input new recipe for an authorized user"
    )
    @jwt_required()
    def post(self):
        """
        Adds a new recipe
        """
        username = get_jwt_identity()

        current_user = User.query.filter_by(username=username).first()

        if current_user:
            data = recipes.payload

            max_recipe_id = Recipe.query.filter_by(user_id=current_user.id).order_by(Recipe.recipe_id.desc()).first()
            new_recipe_id = 1 if max_recipe_id is None else max_recipe_id.recipe_id + 1

            new_recipe = Recipe(
                recipe_id = new_recipe_id,
                pastry_name = data.get('pastry_name'),
                recipe = data.get('recipe'),
                user_id = current_user.id
            )

            new_recipe.save()

            return new_recipe, HTTPStatus.CREATED

        return {'message': 'order not created'}, HTTPStatus.UNAUTHORIZED

@recipes.route('/<int:recipe_id>')
class OneRecipe(Resource):
    @recipes.marshal_with(recipe_model)
    @recipes.doc(
        description="Retrive a recipe of an authorized user by its id",
        params={
            "recipe_id": "id of recipe to retrieve"
        }
    )
    @jwt_required()
    def get(self, recipe_id):
        """
        Displays a particular recipe of an authorized user
        Args:
            recipe_id(int): id of the recipe to display
        """
        username = get_jwt_identity()

        current_user = User.query.filter_by(username=username).first()

        if not current_user:
            return {'message': 'User not found'}, HTTPStatus.NOT_FOUND
        
        recipe = Recipe.query.filter_by(user=current_user, recipe_id=recipe_id).first()

        return recipe, HTTPStatus.OK

    @recipes.expect(input_recipe)
    @recipes.marshal_with(recipe_model)
    @recipes.doc(
        description="Updates a recipe of an authorized user by its id",
        params={
            "recipe_id": "id of recipe to update"
        }
    )
    @jwt_required()
    def put(self, recipe_id):
        """
        Updates a particular recipe
        Args:
            recipe_id(int): id of the recipe to update
        """
        update_recipe = Recipe.query.filter_by(recipe_id=recipe_id).first()

        data = recipes.payload

        if 'pastry_name' in data:
            update_recipe.pastry_name = data['pastry_name']
        if 'recipe' in data:
            update_order.recipe = data['recipe']

        db.session.commit()

        return update_recipe, HTTPStatus.OK

    @recipes.marshal_with(recipe_model)
    @recipes.doc(
        description="Deletes a recipe of an authorized user by its id",
        params={
            "recipe_id": "id of recipe to delete"
        }
    )
    @jwt_required()
    def delete(self, recipe_id):
        """
        Deletes a particular recipe
        Args:
            recipe_id(int): id of the recipe to delete
        """
        recipe = Recipe.query.filter_by(recipe_id=recipe_id).first()
        
        if recipe:
            recipe.delete()

            return recipe, HTTPStatus.NO_CONTENT
        
        return {'message': 'Order Not Found'}, HTTPStatus.NOT_FOUND