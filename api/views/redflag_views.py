from flask import request,jsonify,Flask
from flask_restful import Resource, Api
from api.models.redflag import check_type_date,check_type_list,check_type_string,check_type_int



redflag_records = []
class Records(Resource):
   
      def get(self, id):
            if request.content_type != 'application/json': 
                  return {"error":"format must be json"}
            #data=request.get_json()                        
            for store in redflag_records:
                        if store['id'] == id:
                              return {"status":200,"data":[{'createdBy':store['createdBy'],'id':store['id'],\
                              'comment':store['comment'],'type':store['type'],'createdOn':store['createdOn'],\
                              'location':store['location'],'status':store['status']}]} 
                                                           
                        
                  
      def delete(self, id):
            for store in redflag_records:
                  if store['id'] == id:
                        redflag_records.remove(store)
                  
            return {"status":200,"data":[{"id":id,"message":"red-flag record has been deleted"}]},201

