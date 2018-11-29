from flask import request,Flask

def check_body():
            if request.content_type != 'application/json': 
                  return {"error":"format must be json"}