from flask import request,jsonify,Flask, make_response
from flask_restful import Resource, Api
from api.views.redflag_views import redflag_records
from api.models.redflag import check_type_date,check_type_list,check_type_string,check_type_int
from flask_jwt_extended import create_access_token
from flask_jwt import jwt_required
import datetime
import jwt

secret_key='jose'

users_list = []
class CreateUser(Resource):
      
      def post(self):
            if request.content_type != 'application/json': 
                  return {"error":"format must be json"}
            data=request.get_json()
      
            
            if 'firstname' not in data and 'lastname' not in data and 'othernames'  not in data and 'email' not in data and \
            'phoneNumber' not in data and 'username' not in data and 'registered' not in data and 'isAdmin' not in data and 'password' not in data: 
                  return {"error":"some fields are empty"},400
            
            check_format=[data['firstname'],data['lastname'],data['othernames'],data['email'],data['phoneNumber'],
            data['username'],data['registered'],data['isAdmin']] 
            if not all(isinstance(x,str) for x in check_format):
                  return {"error":"entered a non string where not applicable"}
         
            for users in users_list:
                  if users['email']==data['email'] and users['username']==data['username']:
                        return {'message':"that username {} already exists".format(data['username'])}, 400
            else:
                        id=len(redflag_records)+1
                        users = {'user_id':id, 'firstname':data['firstname'],
                        'lastname':data['lastname'],'email':data['email'],
                        'othernames':data['othernames'],'registered':data['registered'],
                         'username':data['username'],'password':data['password'], 
                         'isAdmin':data['isAdmin'],'phoneNumber':data['phoneNumber']}
                        users_list.append(users)
            return {"status":201,"data":[{"user_id":id,"message":"created user"}]},201    

      
