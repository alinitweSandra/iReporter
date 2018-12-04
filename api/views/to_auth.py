from flask import request,jsonify,Flask
from flask_restful import Resource, Api
from api.views.redflag_views import redflag_records
from api.views.to_logIn import LogIn
from api.views.to_create_users import users_list


class To_Auth(Resource):
    def post(self):
        data=request.get_json()
        return LogIn.user_auth_logic(self,users_list,data['password'],data['username'])