from flask import request,jsonify,Flask
from flask_restful import Resource, Api
from api.views.redflag_views import redflag_records
from api.models.redflag import check_type_date,check_type_list,check_type_string,check_type_int

class Records(Resource):
      
      
    def get(self, id):
            if id == None:
                #not working for the if
                  return {'records': redflag_records}
            else:
                  for store in redflag_records:
                        if store['id'] == id:
                              return {"status":200,"data":[{'createdBy':store['createdBy'],'id':store['id'],
                              'comment':store['comment'],'type':store['type'],'createdOn':store['createdOn'],\
                              'location':store['location'],'status':store['status']}]} 
                       
                  return {'message':'store not found'}

     
    def delete(self,id):
    
            global redflag_records
         
            if check_type_int(self, id) is False:
                  return {'message':"name of item shoulsd be accessed by an int"}
            for items in redflag_records:
                  if items['id']==id:      
                        redflag_records = list(filter(lambda x: x['id'] != id, redflag_records))
            
                        return {'message': 'Item deleted'}
                  else:
                        return {'message': 'Item not found'}
