from flask_restx import Namespace, Resource, fields
from ..models.recipes import Recipe

recipes = Namespace('recipes', description="recipes namespace")

recipe_model = recipes.model(
    'Recipes', {
        'id': fields.Integer(description="id of the recipe"),
        'pastry_name': fields.String(required=True, description="the name of pastry"),
        'recipe': fields.String(required=True, description="instructions on how to make the pastry"),
        'created_at': fields.DateTime(readonly=True, description="date recipe was entered"),
        'updated_at': fields.DateTime(readonly=True, description="date recipe got updated")
    }
)

@recipes.route('/')
class Recipes(Resource):
    @recipes.marshal_with(recipe_model)
    def get(self):
        """
        Display all recipes of the user only
        """
        pass

    def post(self):
        """
        Adds a new recipe
        """
        pass

@recipes.route('/<int:recipe_id>')
class OneRecipe(Resource):
    def get(self, recipe_id):
        """
        Displays a particular recipe
        Args:
            recipe_id(int): id of the recipe to display
        """
        pass

    def put(self, recipe_id):
        """
        Updates a particular recipe
        Args:
            recipe_id(int): id of the recipe to update
        """
        pass

    def delete(self, recipe_id):
        """
        Deletes a particular recipe
        Args:
            recipe_id(int): id of the recipe to delete
        """
        pass