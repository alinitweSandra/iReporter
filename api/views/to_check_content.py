from flask import request,jsonify,Flask


def check_body():

    if request.content_type != 'application/json': 
                  return {"error":"format must be json"},400
    