from flask import request,jsonify,Flask
from flask_restful import Resource, Api
from api.views.redflag_views import redflag_records
from api.models.redflag import check_type_date,check_type_list,check_type_string,check_type_int


class RecordComment(Resource):
    

      def put(self, id):
            if request.content_type != 'application/json': 
                  return {"error":"format must be json"}
            data=request.get_json()
            if 'comment' not in data :
                  return {"error":"the field is empty"}
            if data['comment'] is False:
                  return {"error":"the field has no value"}
            if check_type_string(self,data['comment']) is False:
                  return {"error":"not a list entered"} 
           
            for store in redflag_records:
                  if store['status']!='draft':
                        return {"message":"cant update record due to status value"}
                  if store['id'] == id:
                              
                              #del store['comment'],store['location']
                              del store['comment']
                              store.update({'comment':data['comment']})
                              
            
            return {"status":201,"data":[{"id":id,"message":"uploaded red-flag's comment"}]},201

