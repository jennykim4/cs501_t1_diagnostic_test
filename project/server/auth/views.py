
# project/server/auth/views.py

from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView, View

from project.server import bcrypt, db
from project.server.models import User

from sqlalchemy import inspect

auth_blueprint = Blueprint('auth', __name__)

class RegisterAPI(MethodView):
    """
    User Registration Resource
    """

    def get(self):
    	responseObject = {
    		'status': 'success',
    		'message': 'Request successful but please send an HTTP POST request to register the user.'
    	}
    	return make_response(jsonify(responseObject)), 201

    def post(self):
        # get the post data
        post_data = request.get_json(force=True); print(request)
        # check if user already exists
        user = User.query.filter_by(email=post_data.get('email')).first()
        if not user:
            try:
                user = User(
                    email=post_data.get('email'),
                    password=post_data.get('password')
                )
                # insert the user
                db.session.add(user)
                db.session.commit()
                # generate the auth token
                auth_token = user.encode_auth_token(user.id)
                print(auth_token.decode())
                responseObject = {

                    'status': 'success',
                    'message': 'Successfully registered.',
                    
<<<<<<< HEAD
                    'auth_token': auth_token.decode()
                }
            
                # print (auth_token)
=======
                    'auth_token': auth_token
                }
            
                print (auth_token)
>>>>>>> 3a23254d684483a0a43c57aae5c0658ea11bfa19
                return make_response(jsonify(responseObject)), 201

            except Exception as e:
                print (e)
                responseObject = {
                    'status': 'fail',
                    'message': 'Some error occurred. Please try again.'
                }
                return make_response(jsonify(responseObject)), 401
        else:
            responseObject = {
                'status': 'fail',
                'message': 'User already exists. Please Log in.',
            }
            return make_response(jsonify(responseObject)), 202


# define the API resources
registration_view = RegisterAPI.as_view('register_api')

# add Rules for API Endpoints
auth_blueprint.add_url_rule(
    '/auth/register',
    view_func=registration_view,
    methods=['POST', 'GET']
)



class ShowUsersAPI(MethodView):
    """
    User List Resource
    """

<<<<<<< HEAD
    def get(self): 
=======
    def get(self):
>>>>>>> 3a23254d684483a0a43c57aae5c0658ea11bfa19
        list_of_all_users = User.query.all()
        users = [
    		user.email for user in list_of_all_users
    	]
        print(users)
        return make_response(jsonify(users)), 201
       



# define the API resources
<<<<<<< HEAD
users_view = ShowUsersAPI.as_view('ShowUsers_api')
=======
user_view = ShowUsersAPI.as_view('ShowUsers_api')
>>>>>>> 3a23254d684483a0a43c57aae5c0658ea11bfa19

# add Rules for API Endpoints
auth_blueprint.add_url_rule(
    '/users/index',
<<<<<<< HEAD
    view_func=users_view,
    methods=['GET']
)
=======
    view_func=user_view,
    methods=['GET']
)

    methods=['POST', 'GET']
)
>>>>>>> 3a23254d684483a0a43c57aae5c0658ea11bfa19
