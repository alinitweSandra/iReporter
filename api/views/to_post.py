from flask import request,jsonify,Flask
from flask_restful import Resource, Api
from api.views.redflag_views import redflag_records
from api.models.redflag import check_type_date,check_type_list,check_type_string,check_type_int
from api.views.to_check_content import check_body
import datetime
from api.helper.jwt_required import token_required
from api.views.to_create_users import users_list

class RecordList(Resource):    
           
      def get(self):   
      
            return {"status":200,"data": redflag_records},200
      @token_required
      def post(self,current_user):
            if request.content_type != 'application/json': 
                  return {"status":400,"error":"format must be json"},400
            data=request.get_json() 
            now = datetime.datetime.now()    
                
            check_data=['comment','location','type']
            for check_data in check_data:
                  if check_data not in data:
                        return {"status":400,"error":"ensure all fields are filled"},400
            
            check_format=[data['comment'],data['type']] 
            if not all(isinstance(x,str) for x in check_format):
                  return {"status":400,"error":"enter only strings"},400
            # if check_type_int(self,data['createdBy'])is False:
            #       return {"status":400,"error":"createdBy: integer"},400

            if check_type_list(self,data['location'])is False:
                  return {"status":400,"error":"location: list"},400

            for items in redflag_records:
                  if items['location']==data['location']:
                        return {"status":400,"message":"{} exists".format('createdBy')}, 400
            else:
                  for user in users_list:
                        if user['username']==current_user:
                              user_id=user['user_id']
                        id=len(redflag_records)+1
                        item = {'id':id, 'createdOn':now.strftime("%Y-%m-%d"),
                        'createdBy':user_id,'type':data['type'],
                        'location':data['location'],'status':'draft', 'comment':data['comment']}
                        redflag_records.append(item)
            return {"status":201,"data":[{"id":id,"message":"created red-flag record"}]},201                                     