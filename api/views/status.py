from flask import request,jsonify,Flask
from flask_restful import Resource, Api
from api.views.redflag_views import redflag_records
from api.models.redflag import check_type_date,check_type_list,check_type_string,check_type_int
from api.models.check_content import check_body


class RecordStatus(Resource):
    

      def put(self, id):
            check_body()
            data=request.get_json()
            if 'status' not in data :
                  return {"error":"the field is empty"}
            if data['status'] is False:
                  return {"error":"the field has no value"}
            if check_type_string(self,data['status']) is False:
                  return {"error":"not a string entered"} 
           
            for store in redflag_records:
                        if store['id'] == id:
                              
                              del store['status']
                              item = {'status': data['status']}
            redflag_records.append(item)
            
            return {"status":201,"data":[{"id":id,"message":"uploaded red-flag's record"}]},201

