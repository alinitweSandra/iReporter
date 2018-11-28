from flask import Flask
from flask_restful import Api

from api.views.status import RecordStatus



app = Flask(__name__)
api=Api(app)
  

api.add_resource(RecordStatus, '/api/v1/red-flags/<int:id>')  

