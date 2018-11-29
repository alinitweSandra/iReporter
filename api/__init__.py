from flask import Flask
from flask_restful import Api
from api.views.comments import RecordComment
from api.views.redflag_views import Records
from api.views.to_post import RecordList
from api.views.status import RecordStatus
from api.views.location import RecordLocation
from flask_jwt import JWT,jwt_required

from api.views.to_create_users import CreateUser
from api.views.to_auth import To_Auth


app = Flask(__name__)
secret_key = "jose"
api=Api(app)


# to create users url
api.add_resource(CreateUser, '/api/v1/create-users') 

api.add_resource(RecordList, '/api/v1/red-flags')    
api.add_resource(Records, '/api/v1/red-flags/<int:id>') 
api.add_resource(RecordComment, '/api/v1/red-flags/<int:id>')
api.add_resource(RecordStatus, '/api/v1/red-flags/<int:id>') 
api.add_resource(RecordLocation, '/api/v1/red-flags/<int:id>') 

# to log in
api.add_resource(To_Auth, '/api/v1/auth/login') 
