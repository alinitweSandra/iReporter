from flask import request,jsonify,Flask


def check_body():

    if request.content_type != 'application/json': 
                  return {"error":"format must be json"},400
    
def check_instance(alist):
    if not all(isinstance(x,str) for x in alist):
                  return {"status":400,"error":"enter only strings"},400