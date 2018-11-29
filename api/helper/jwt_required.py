"""
This module defines the user auth decorator function

"""
from functools import wraps
import jwt
from flask import request
from flask import jsonify
from api.views.to_logIn import secret_key
from api.views.to_create_users import users_list




def token_required(f):
    """
    function to authenticate users at the endpoints
    """
    @wraps(f)
    def decorated(self, *args, **kwargs):
        token = None
        if 'token' in request.headers:
            token = request.headers['token']
        if not token:
            return {'message':'Token is missing!'}, 401
        try:
            data = jwt.decode(token, secret_key, algorithm='HS256')
            user_username = data['username']
            #users_list = AUTH_USERS .users
            for user in users_list:
                if user_username == user['username'] and user['isAdmin']== 'yes':
                    current_user = user
        except:
            return {'message':'Token is invalid!'}, 401
        return f(self, current_user, *args, **kwargs)
    return decorated