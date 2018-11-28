from flask import request,jsonify,Flask
from flask_restful import Resource, Api
from api.views.redflag_views import redflag_records
from api.models.redflag import check_type_date,check_type_list,check_type_string,check_type_int

class RecordList(Resource):    
           
      def get(self):
           
              return {'records': redflag_records}

      def post(self):
            if request.content_type != 'application/json': 
                  return {"error":"format must be json"}
            data=request.get_json()
      
            
            if 'createdBy' not in data and 'createdOn' not in data and 'status'  not in data and 'comment' not in data and \
            'location' not in data and 'type' not in data: 
                  return {"error":"some fields are empty"},400
            
            check_format=[data['createdBy'],data['comment'],data['status'],data['type'],data['createdOn']] 
            if not all(isinstance(x,str) for x in check_format):
                  return {"error":"entered a non string where not applicable"}
            if check_type_list(self,data['location'])is False:
                  return {"error":"wrong location format"} 
            for items in redflag_records:
                  if items['createdBy']==data['createdBy'] and items['status']==data['status'] and items['location']==data['location']:
                        return {'message':"an item {} already exists".format(data['createdBy'])}, 400
            else:
                        id=len(redflag_records)+1
                        item = {'id':id, 'createdOn':data['createdOn'],
                        'createdBy':data['createdBy'],'type':data['type'],
                        'location':data['location'],'status':data['status'], 'comment':data['comment']}
                        redflag_records.append(item)
            return {"status":201,"data":[{"id":id,"message":"created red-flag record"}]},201                                     