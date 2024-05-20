from flask_restx import Namespace, Resource


order = Namespace('order', description="orders namespace")


@order.route('/')
class Orders(Resource):
    def get(self):
        return {'order': 'hello order!'}