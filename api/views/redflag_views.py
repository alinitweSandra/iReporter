from flask import request,jsonify,Flask
from flask_restful import Resource, Api
from api.models.redflag import check_type_date,check_type_list,check_type_string,check_type_int
from flask_jwt import jwt_required
from api.helper.jwt_required import token_required
from api.views.to_check_content import check_body

redflag_records = []

class Records(Resource):
      #@token_required
      def get(self, id):
            check_body()
           
            #data=request.get_json()                        
            for store in redflag_records:
                        if store['id'] == id:
                              return {"status":200,"data":[{'createdBy':store['createdBy'],'id':store['id'],\
                              'comment':store['comment'],'type':store['type'],'createdOn':store['createdOn'],\
                              'location':store['location'],'status':store['status']}]} 
                                                           
                        
                  
      def delete(self, id):
            if request.content_type != 'application/json': 
                  return {"error":"format must be json"}
            data=request.get_json()      
            
            if 'createdBy' not in data: 
                  return {"error":"created by field is empty"},400
            

            if check_type_string(self,data['createdBy'])is False:
                  return {"error":"wrong createdBy format"} 
            for store in redflag_records:
                  if store['createdBy']!=data['createdBy']:
                        return {"error":"please enter the right username in order to delete"}
                  if store['status']!='draft':
                        return {"message":"cant delete record due to status value"}
                  if store['id'] == id:
                        redflag_records.remove(store)
                  
            return {"status":200,"data":[{"id":id,"message":"red-flag record has been deleted"}]},201

