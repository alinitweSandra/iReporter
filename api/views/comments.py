from flask import request,jsonify,Flask
from flask_restful import Resource, Api
from api.views.redflag_views import redflag_records
from api.models.redflag import check_type_date,check_type_list,check_type_string,check_type_int
from api.helper.jwt_required import token_required
from api.views.to_check_content import check_body


class RecordComment(Resource):
    
      @token_required
      def put(self, current_user,id):
            check_body()
            data=request.get_json()

            if 'comment' not in data :
                  return {"error":"the field is empty"}
            if data['comment'] is False:
                  return {"error":"the field has no value"}
            if check_type_string(self,data['comment']) is False:
                  return {"error":"not a list entered"}
                  # it stops here when admin is yes
            if current_user['isAdmin']!="no":
                  return {"error":"you don't have rights"} 

            for store in redflag_records:
                  if store['status']!='draft':
                        return {"message":"cant update record due to status value"}
                  if store['id'] == id:
                              
                              #del store['comment'],store['location']
                              del store['comment']
                              store.update({'comment':data['comment']})
                              
            
            return {"status":201,"data":[{"id":id,"message":"uploaded red-flag's comment"}]},201

