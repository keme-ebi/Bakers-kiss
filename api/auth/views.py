from flask_restx import Namespace, Resource


auth = Namespace('auth', description="authentication namespace")


@auth.route('/signup')
class SignUp(Resource):
    def post(self):
        """
        Signs up/Creates a new user
        """
        pass

auth.route('/login')
class Login(Resource):
    def post(self):
        """
        Logs in user using JWT pair
        """
        pass