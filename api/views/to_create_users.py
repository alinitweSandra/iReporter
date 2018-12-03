from flask import request,jsonify,Flask, make_response
from flask_restful import Resource, Api

from api.models.redflag import check_type_date,check_type_list,check_type_string,check_type_int,check_type_bool
from flask_jwt_extended import create_access_token
from flask_jwt import jwt_required
import datetime
import jwt
from api.views.to_check_content import check_body

secret_key='jose'

users_list = []
class CreateUser(Resource):
      
      def post(self):
            if request.content_type != 'application/json': 
                  return {"status":400,"error":"format must be json"},400
            data=request.get_json()

            check_data=['firstname','lastname','othernames','email','username','registered','phoneNumber','password','isAdmin']
            for check_data in check_data:
                  if check_data not in data:
                        return {"status":400,"error":"ensure all fields are filled"},400
            
            check_format=[data['firstname'],data['lastname'],data['othernames'],data['email'],data['phoneNumber'],
            data['username']] 
            if not all(isinstance(x,str) for x in check_format):
                  return {"status":400,"error":"enter only strings"},400
            if check_type_bool(self,data['isAdmin']) is False:
                  return {"error":"isAdmin: boolean"},400
            if check_type_date(self,data['registered']) is False:
                  return {"status":400,"error":"registered:  dd/mm/yyyy"},400
            
         
            for users in users_list:
                  if users['email']==data['email'] and users['username']==data['username']:
                        return {"status":400,'message':"{} exists".format(data['username'])}, 400
            else:
                        id=len(users_list)+1
                        users = {'user_id':id, 'firstname':data['firstname'],
                        'lastname':data['lastname'],'email':data['email'],
                        'othernames':data['othernames'],'registered':data['registered'],
                         'username':data['username'],'password':data['password'], 
                         'isAdmin':data['isAdmin'],'phoneNumber':data['phoneNumber']}
                        users_list.append(users)
            return {"status":201,"data":[{"user_id":id,"message":"created user"}]},201      
