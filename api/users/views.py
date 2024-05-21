from flask_restx import Namespace, Resource

user = Namespace('user', description="orders namespace")


# User
@user.route('/<int:user_id>')
class User(Resource):
    def get(self, user_id):
        """
        Displays all orders and recipes for user
        Args:
            user_id(int): id to get from the database
        """
        pass

    def put(self, user_id):
        """
        Updates user by the id
        Args:
            user_id(int): id to update in the database
        """
        pass


# User orders
@user.route('/<int:user_id>/orders')
class UserOrders(Resource):
    def get(self, user_id):
        """
        Displays all orders of the user only
        Args:
            user_id(int): id to get all orders from
        """
        pass

    def post(self, user_id):
        """
        Creates a new order for user
        Args:
            user_id(int): id to post new order into
        """
        pass

@user.route('/<int:user_id>/orders/<int:order_id>')
class UserOneOrder(Resource):
    def get(self, user_id, order_id):
        """
        Displays a particular order
        Args:
            user_id(int): id to get orders from
            order_id(int): id to get specific order
        """
        pass

    def put(self, user_id, order_id):
        """
        Updates a particular order
        Args:
            user_id(int): id to get orders from
            order_id(int): id to get specific order to update
        """
        pass

    def delete(self, user_id, order_id):
        """
        Deletes a particular order
        Args:
            user_id(int): id to get orders from
            order_id(int): id to get specific order to delete
        """
        pass


# User recipes
@user.route('/<int:user_id>/recipes')
class UserRecipes(Resource):
    def get(self, user_id):
        """
        Display all recipes of the user only
        Args:
            user_id(int): id to get all recipes from
        """
        pass

@user.route('/<int:user_id>/recipes/<int:recipe_id>')
class UserOneRecipe(Resource):
    def get(self, user_id, recipe_id):
        """
        Displays a particular recipe
        Args:
            user_id(int): id of the user to get recipes from
            recipe_id(int): id of the recipe to display
        """
        pass

    def put(self, user_id, recipe_id):
        """
        Updates a particular recipe
        Args:
            user_id(int): id of the user to get recipes from
            recipe_id(int): id of the recipe to update
        """
        pass

    def delete(self, user_id, recipe_id):
        """
        Deletes a particular recipe
        Args:
            user_id(int): id of the user to get recipes from
            recipe_id(int): id of the recipe to delete
        """
        pass