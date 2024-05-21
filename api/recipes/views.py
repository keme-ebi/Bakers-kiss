from flask_restx import Namespace, Resource

recipes = Namespace('recipes', description="recipes namespace")


@recipes.route('/')
class Recipes(Resource):
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