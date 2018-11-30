from flask import request,jsonify,Flask
from flask_restful import Resource, Api
from api.models.redflag import check_type_date,check_type_list,check_type_string,check_type_int
from flask_jwt import jwt_required
from api.helper.jwt_required import token_required
from api.views.to_check_content import check_body
from api.views.to_create_users import users_list

redflag_records = []

class Records(Resource):
      @token_required
      def get(self, current_user, id):
            check_body()
            for user in users_list:
                  if current_user == user['username'] and user['isAdmin'] is True:
                        for store in redflag_records:
                              if store['id'] == id:
                                    return {"status":200,"data":[{'createdBy':store['createdBy'],'id':store['id'],\
                                    'comment':store['comment'],'type':store['type'],'createdOn':store['createdOn'],\
                                    'location':store['location'],'status':store['status']}]} 
                  else:
                             
      
                         return {"error":"you dont have the rights"} 
                                                            
                        
      @token_required            
      def delete(self, current_user, id):
            check_body()
            data=request.get_json()      
            
            if 'createdBy' not in data: 
                  return {"error":"created by field is empty"},400
            

            if check_type_string(self,data['createdBy'])is False:
                  return {"error":"wrong createdBy format"} 
            for user in users_list:
                  if current_user == user['username'] and user['isAdmin'] is False:
                  
                        for store in redflag_records:
                              
                              if store['status']!='draft':
                                    return {"message":"cant delete record due to status value"}
                              if store['id'] == id:
                                    redflag_records.remove(store)
                              
                        return {"status":200,"data":[{"id":id,"message":"red-flag record has been deleted"}]},201

