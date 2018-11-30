from flask import request,jsonify,Flask
from flask_restful import Resource, Api
from api.views.redflag_views import redflag_records
from api.models.redflag import check_type_date,check_type_list,check_type_string,check_type_int
from api.views.to_create_users import users_list


class RecordStatus(Resource):
    

      def put(self, id):
            if request.content_type != 'application/json': 
                   return {"error":"format must be json"}
            data=request.get_json()
            if 'status' not in data and 'location' not in data :
                   return {"error":"the field is empty"}
            for users in users_list:
                  if users['isAdmin']=='yes':
                        if data['status'] is False:
                             return {"error":"the field has no value"}
                        if check_type_string(self,data['status']) is False:
                              return {"error":"not a string entered"}
                        for store in redflag_records:
                              
                              if store['id'] == id:
                                          
                                          #del store['comment'],store['location']
                                          del store['status']
                                          store.update({'status':data['status']})
                        
                        
                        return {"status":201,"data":[{"id":id,"message":"uploaded red-flag's record status"}]},201
                  
                  else:
                        if data['location'] is False:
                             return {"error":"the field has no value"}
                        if check_type_list(self,data['location']) is False:
                              return {"error":"not a string entered"}
                        for store in redflag_records:
                              
                              if store['id'] == id:
                                    if store['status']!='draft':
                                          return {"error":"cant update due to status"}
                                                                             
                                    del store['location']
                                    store.update({'location':data['location']})
                        
                        
                        return {"status":201,"data":[{"id":id,"message":"uploaded red-flag's record comment"}]},201

            
            