from flask_restx import Namespace, Resource

orders = Namespace('orders', description="orders namespace")


@orders.route('/')
class Orders(Resource):
    def get(self):
        """
        Displays all orders of the user only
        """
        pass

    def post(self):
        """
        Creates a new order for user
        """
        pass

@orders.route('/<int:order_id>')
class OneOrder(Resource):
    def get(self, order_id):
        """
        Displays a particular order
        Args:
            order_id(int): id to get specific order
        """
        pass

    def put(self, order_id):
        """
        Updates a particular order
        Args:
            order_id(int): id to get specific order to update
        """
        pass

    def delete(self, order_id):
        """
        Deletes a particular order
        Args:
            order_id(int): id to get specific order to delete
        """
        pass