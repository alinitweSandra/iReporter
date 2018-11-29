from api.views.to_create_users import users_list

username_mapping={u.username:u for u in users_list}
userid_mapping={u.id:u for u in users_list}

# def authenticate(username,password):
#     user = username_mapping.get(username,None)
#     if user and user.password==password:
#         return user

def authenticate(username, password):
    if not (username and password):
        return False
    user = username_mapping.get(username,None)
    if user and user.password==password:
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id,None)