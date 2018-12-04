from flask import request,jsonify,Flask
from flask_restful import Resource, Api
from api.views.redflag_views import redflag_records
from api.models.redflag import check_type_date,check_type_list,check_type_string,check_type_int
from api.views.to_create_users import users_list
from api.helper.jwt_required import token_required
from api.views.to_check_content import check_body


class RecordStatus(Resource):
    

      @token_required
      def put(self,current_user, id):
            if request.content_type != 'application/json': 
                  return {"status":400,"error":"format must be json"},400
            data=request.get_json()
            for users in users_list:
                  if users['isAdmin']==True:
                        if 'status' not in data:
                              return {"status":400,"error":"empty status field"},400
                  
                        if data['status'] is False:
                              return {"status":400,"error":"update status field"},400
                        if check_type_string(self,data['status']) is False:
                              return {"status":400,"error":"status: string"},400
                        status_list=('rejected','resolved','under_investigation')
                        for store in redflag_records:
                              
                              if store['id'] == id:
                                    if data['status'] not in status_list:
                                          return{"status":400,"error":"status:('rejected','resolved','under_investigation')"},400
                                          
                                          #del store['comment'],store['location']
                                    del store['status']
                                    store.update({'status':data['status']})
                        
                  
                        return {"status":201,"data":[{"id":id,"message":"uploaded red-flag's record status"}]},201

            
                        
                  else:
                        if 'location' not in data:
                              return {"status":400,"error":"empty location field"},400
                        if data['location'] is False:
                              return {"status":400,"error":"update location field"},400
                        if check_type_list(self,data['location']) is False:
                              return {"status":400,"error":"location: list"},400
                        for store in redflag_records:
                              
                              if store['id'] == id:
                                    if store['status']!='draft':
                                          return {"status":400,"error":"cant update due to status"},400
                                                                              
                                    del store['location']
                                    store.update({'location':data['location']})
                        
                        
                        return {"status":201,"data":[{"id":id,"message":"uploaded red-flag's record location"}]},201

                        # if 'comment' not in data:
                        #       return {"status":400,"error":"empty comment field"},400
                        # if data['comment'] is False:
                        #       return {"status":400,"error":"update comment field"},400
                        # if check_type_string(self,data['comment']) is False:
                        #       return {"status":400,"error":"comment: string"},400
                        # for store in redflag_records:
                        
                        #       if store['id'] == id:
                        #             if store['status']!='draft':
                        #                   return {"status":400,"error":"cant update due to status"},400
                                                                        
                        #             del store['comment']
                        #             store.update({'comment':data['comment']})
                  
                  
                        # return {"status":201,"data":[{"id":id,"message":"uploaded red-flag's record comment"}]},201

                  