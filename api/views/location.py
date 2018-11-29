from flask import request,jsonify,Flask
from flask_restful import Resource, Api
from api.views.redflag_views import redflag_records
from api.models.redflag import check_type_date,check_type_list,check_type_string,check_type_int


class RecordLocation(Resource):
    

      def put(self, id):
            if request.content_type != 'application/json': 
                  return {"error":"format must be json"}
            data=request.get_json()
            if 'location' not in data :
                  return {"error":"the field is empty"}
            if data['location'] is False:
                  return {"error":"the field has no value"}
            if check_type_list(self,data['location']) is False:
                  return {"error":"not a list entered"} 
           
            for store in redflag_records:
                if store['status']!='draft':
                    return {"message":"cant update location due to status value"}
                for store in redflag_records:
                        if store['status']!='draft':
                              return {"message":"cant update record due to status value"}
                        if store['id'] == id:
                              
                              #del store['comment'],store['location']
                              del store['location']
                              store.update({'location':data['location']})
                              
            return {"status":201,"data":[{"id":id,"message":"uploaded red-flag's location"}]},201

