from flask import Flask
from flask_restful import Api
from api.views.comments import RecordComment
from api.views.redflag_views import Records
from api.views.to_post import RecordList
from api.views.status import RecordStatus


app = Flask(__name__)
api=Api(app)
api.add_resource(RecordList, '/api/v1/red-flags')    
api.add_resource(Records, '/api/v1/red-flags/<int:id>') 
api.add_resource(RecordComment, '/api/v1/red-flags/<int:id>/<string:name>')
api.add_resource(RecordStatus, '/api/v1/red-flags/<int:id>')   
 
