from flask_restx import Namespace, Resource


auth = Namespace('auth', description="authentication namespace")


@auth.route('/')
class HelloWord(Resource):
    def get(self):
        return {'data': 'hello world!'}