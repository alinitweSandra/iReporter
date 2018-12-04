
from unittest import TestCase
from flask import json
from api import app


class Tests(TestCase):
    """
       Class to test end points 
    """ 
    def setUp(self):
        self.app = app
        self.client = self.app.test_client
        self.new_user = {"firstname":"aheebwa",
                        "lastname":"kukute",
                        "othernames":"bob",
                        "email":"sandraalinitwe@gmail.com",
                        "phoneNumber":"256757852937",
                        "username":"user",
                        "registered":"29/09/2015",
                        "isAdmin":False,
                        "password":"user"
  
        }
     


        self.login_credentials_admin = {
            "username":"admin",
            "password":"admin"
        }

        self.login_credentials_user = {
            "username":"user",
            "password":"user"
        }  
        self.client().post(
            '/api/v1/create-users', content_type='application/json',
            data=json.dumps(
                dict(
                    firstname=self.new_user['firstname'], lastname=self.new_user['lastname'],
                    email=self.new_user['email'], phoneNumber=self.new_user['phoneNumber'],
                    username=self.new_user['username'], password=self.new_user['password'],
                    isAdmin=self.new_user['isAdmin'],
                    othernames=self.new_user['othernames']
                )
            )
        )


        user_login_result = self.client().post(
            '/api/v1/auth/login', content_type='application/json',
            data=json.dumps(
                dict(
                    username=self.login_credentials_user['username'],
                    password=self.login_credentials_user['password']
                )
            )
        )

        admin_login_result = self.client().post(
            '/api/v1/auth/login', content_type='application/json',
            data=json.dumps(
                dict(
                    username=self.login_credentials_admin['username'],
                    password=self.login_credentials_admin['password']
                )
            )
        )
        self.result = json.loads(user_login_result.data)
        self.user_generated_token = self.result['token_generated']
        self.result2 = json.loads(admin_login_result.data)
        #self.admin_generated_token = self.result2['token_generated']


    def test_add_user_with_empty_fields(self):
        """
           method to test adding a user with empty fields
        """  
        post_result = self.client().post('/api/v1/create-users', content_type = 'application/json',
                                         data=json.dumps(dict()))
        self.assertEqual(post_result.status_code, 400) 

    def test_add_int_firstname(self):
        """
           method to add firstname as integer
        """  
        post_result = self.client().post('/api/v1/create-users', content_type='application/json',   data=json.dumps(
                                         dict(
                    firstname=1, lastname='lastname',
                    email='email', phoneNumber='phoneNumber',
                    username='username', password='password',
                    isAdmin='isAdmin', 
                    othernames='othernames'   )))

 
        
        
        self.assertEqual(post_result.status_code, 400)   
        json_data = json.loads(post_result.data)      
        assert json_data['status'] == 400
        self.assertTrue(post_result.json["error"], "enter only string") 
        
 
        
        
    def test_add_int_lastname(self):
        """
           method to add lastname as integer
        """  
        post_result = self.client().post('/api/v1/create-users', content_type='application/json',   data=json.dumps(
                                         dict(
                    firstname='firstname', lastname=1,
                    email='email', phoneNumber='phoneNumber',
                    username='username', password='password',
                    isAdmin='isAdmin', 
                    othernames='othernames'   )))

 
        
        
        self.assertEqual(post_result.status_code, 400)   
        json_data = json.loads(post_result.data)      
        assert json_data['status'] == 400
        self.assertTrue(post_result.json["error"], "enter only string") 
        
            
    def test_add_int_phoneNumber(self):
        """
           method to add phoneNumber as integer
        """  
        post_result = self.client().post('/api/v1/create-users', content_type='application/json',   data=json.dumps(
                                         dict(
                    firstname='firstname', lastname='lastname',
                    email='email', phoneNumber=1,
                    username='username', password='password',
                    isAdmin='isAdmin', 
                    othernames='othernames'   )))

 
        
        
        self.assertEqual(post_result.status_code, 400)   
        json_data = json.loads(post_result.data)      
        assert json_data['status'] == 400
        self.assertTrue(post_result.json["error"], "enter only string") 

    def test_add_int_email(self):
        """
           method to add email as integer
        """  
        post_result = self.client().post('/api/v1/create-users', content_type='application/json',   data=json.dumps(
                                         dict(
                    firstname='firstname', lastname='lastname',
                    email=1, phoneNumber='phoneNumber',
                    username='username', password='password',
                    isAdmin='isAdmin',
                    othernames='othernames'   )))

 
        
        
        self.assertEqual(post_result.status_code, 400)   
        json_data = json.loads(post_result.data)      
        assert json_data['status'] == 400
        self.assertTrue(post_result.json["error"], "enter only string")

    def test_add_int_othername(self):
        """
        method to add othername as integer
        """  
        post_result = self.client().post('/api/v1/create-users', content_type='application/json',   data=json.dumps(
                                         dict(
                    firstname='firstname', lastname='lastname',
                    email=1, phoneNumber='phoneNumber',
                    username='username', password='password',
                    isAdmin=False,
                    othernames=1   )))

 
        
        
        self.assertEqual(post_result.status_code, 400)   
        json_data = json.loads(post_result.data)      
        assert json_data['status'] == 400
        self.assertTrue(post_result.json["error"], "enter only string")
    
    def test_add_int_username(self):
        """
           method to add username as integer
        """  
        post_result = self.client().post('/api/v1/create-users', content_type='application/json',   data=json.dumps(
                                         dict(
                    firstname='firstname', lastname='lastname',
                    email=1, phoneNumber='phoneNumber',
                    username='username', password='password',
                    isAdmin='isAdmin',
                    othernames='othernames'   )))

 
        
        
        self.assertEqual(post_result.status_code, 400)   
        json_data = json.loads(post_result.data)      
        assert json_data['status'] == 400
        self.assertTrue(post_result.json["error"], "enter only string")
    
    
    def test_add_int_isAdmin(self):
        """
           method to add isAdmin as integer
        """  
        post_result = self.client().post('/api/v1/create-users', content_type='application/json', data=json.dumps(
                                         dict(
                    firstname='firstname', lastname='lastname',
                    email=1, phoneNumber='phoneNumber',
                    username='username', password='password',
                    isAdmin='isAdmin', 
                    othernames='othernames'   )))

 
        
        
        self.assertEqual(post_result.status_code, 400)   
        json_data = json.loads(post_result.data)      
        assert json_data['status'] == 400
        self.assertTrue(post_result.json["error"], "isAdmin: boolean")


    def test_add_record(self):
        """
           method to add a record
        """  
        post_result = self.client().post('/api/v1/red-flags',headers={"token": self.user_generated_token}, content_type='application/json',   data=json.dumps(dict(                                         
                                            type= "cfgv",
                                            location= [9,8],
                                            comment= "fcgvbhj",        
                                            )))
 
        
        
        self.assertEqual(post_result.status_code, 201)   
        json_data = json.loads(post_result.data)      
        assert json_data['status'] == 201
        assert json_data['data'][0] == {"id": 1,"message": "created red-flag record"} 
    
    
    def test_add_record_with_int_type(self):
        """
           method to add type as integer
        """  
        post_result = self.client().post('/api/v1/red-flags',headers={"token": self.user_generated_token}, content_type='application/json',   data=json.dumps(dict(                                         
                                            type= 4,
                                            location= [9,8],
                                            comment= "fcgvbhj",        
                                            )))
 
        
        
        self.assertEqual(post_result.status_code, 400)   
        json_data = json.loads(post_result.data)      
        assert json_data['status'] == 400
        self.assertTrue(post_result.json["error"], "enter only string")
    

    def test_add_record_with_int_comment(self):
        """
           method to add comment as integer
        """  
        post_result = self.client().post('/api/v1/red-flags',headers={"token": self.user_generated_token}, content_type='application/json',   data=json.dumps(dict(                                         
                                            type= "type",
                                            location= [9,8],
                                            comment= 1,        
                                            )))
 
        
        
        self.assertEqual(post_result.status_code, 400)   
        json_data = json.loads(post_result.data)      
        assert json_data['status'] == 400
        self.assertTrue(post_result.json["error"], "enter only string") 
    



    def test_add_record_with_int_location(self):
        """
           method to add location as integer
        """  
        post_result = self.client().post('/api/v1/red-flags',headers={"token": self.user_generated_token}, content_type='application/json',   data=json.dumps(dict(                                         
                                            type= "type",
                                            location= 4,
                                            comment= "fcgvbhj",        
                                            )))
 
        
        
        self.assertEqual(post_result.status_code, 400)   
        json_data = json.loads(post_result.data)      
        assert json_data['status'] == 400
        self.assertTrue(post_result.json["error"], "location: list") 

    
    def test_add_record_with_string_location(self):
        """
           method to add location as string
        """  
        post_result = self.client().post('/api/v1/red-flags',headers={"token": self.user_generated_token}, content_type='application/json',   data=json.dumps(dict(                                         
                                            type= "type",
                                            location= "4",
                                            comment= "fcgvbhj",        
                                            )))
 
        
        
        self.assertEqual(post_result.status_code, 400)   
        json_data = json.loads(post_result.data)      
        assert json_data['status'] == 400
        self.assertTrue(post_result.json["error"], "location: list")







    def test_add_record_with_empty_fields(self):
        """
           method to test adding a record with empty fields
        """  
        post_result = self.client().post('/api/v1/red-flags',headers={"token": self.user_generated_token}, content_type = 'application/json',
                                         data=json.dumps(dict()))
        self.assertEqual(post_result.status_code, 400) 
    
    
    
    def test_get_non_record(self) :  
        """
        method to get a record that doesnt exist
        """
        get_result = self.client().get('/api/v1/red-flags/qwer',headers={"token": self.user_generated_token})
        self.assertEqual(get_result.status_code, 404)


    
    
    def test_get_record(self):
        """
           method to get a specific record
        """
        get_result = self.client().get('/api/v1/red-flags/1',headers={"token": self.user_generated_token})
        self.assertEqual(get_result.status_code, 200)   
    

    def test_get_records(self):
        """
           method to get all records
        """
        get_result = self.client().get('/api/v1/red-flags')
        response = json.loads(get_result.data.decode("utf8"))
        self.assertEqual(get_result.status_code, 200)
        self.assertIsInstance(response, dict)

    def test_no_redflags(self):
        """
           method to test an empty specific record dictionary
        """
        get_result = self.client().get('/api/v1/red-flags')
        self.assertEqual(get_result.status_code, 200)   
        json_data = json.loads(get_result.data)      
        assert json_data['status'] == 200
       
    def test_delete_item(self) :  
        """
           method to test a record to be deleted
        """
        get_result = self.client().delete('/api/v1/red-flags/1',headers={"token": self.user_generated_token})
        self.assertEqual(get_result.status_code, 200)

 

    def test_delete_non_item(self) :  
        """
           method to delete a record that doesnot exxist
        """
        get_result = self.client().delete('/api/v1/red-flags/delete',headers={"token": self.user_generated_token})
        self.assertEqual(get_result.status_code, 404)
    


    def test_update_record(self) :  
        """
            method to test a record to be updated
        """
        get_result = self.client().get('/api/v1/red-flags/1',headers={"token": self.user_generated_token})
        self.assertEqual(get_result.status_code, 200)

        
    def test_update_a_non_existing_item(self) :  
        """
            method to test a record to be updated
        """
        get_result = self.client().get('/api/v1/red-flags/not',headers={"token": self.user_generated_token})
        self.assertEqual(get_result.status_code, 404)



