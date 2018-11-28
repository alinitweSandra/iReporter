from flask import Flask
from flask_restful import Api

from api.views.redflag_views import Records



app = Flask(__name__)
api=Api(app)
  
api.add_resource(Records, '/api/v1/red-flags/<int:id>')  

