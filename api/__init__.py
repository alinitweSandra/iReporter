from flask import Flask
from flask_restful import Api

from api.views.comments import RecordComment



app = Flask(__name__)
api=Api(app)
  

api.add_resource(RecordComment, '/api/v1/red-flags/<int:id>/<string:name>')  

