from flask import request,jsonify,Flask
from flask_restful import Resource, Api

from api.models.redflag import check_type_date,check_type_list,check_type_string,check_type_int
import jwt
import datetime

secret_key='jose'
class LogIn():
    def user_auth_logic(self,alist,username,password):
        for user in alist:
            if username == user['username']:
                if password == user['password']:
                    # if id1 ==user['id']:
                    token = jwt.encode({'username':username, 'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},secret_key,  algorithm='HS256')
                return {'token_generated':token.decode('UTF-8')},200
            return {"status":401,"message":"Wrong Username or Password!!"},401
        


