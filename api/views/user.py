from api.views.to_create_users import users_list
class User:
    def __init__(self, _id, firstname,lastname,othernames,email, phonenumber,username,registered,isAdmin,password):
        self.id=_id
        self.username=username
        self.email=email
        self.firstname=firstname
        self.lastname=lastname
        self.othernames=othernames
        self.isAdmin=isAdmin
        self.phonenumber=phonenumber
        self.registered=registered
        self.password=password
   