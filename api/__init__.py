from flask import Flask
from flask_restful import Api

from api.views.to_post import RecordList



app = Flask(__name__)
api=Api(app)
api.add_resource(RecordList, '/api/v1/red-flags')    

