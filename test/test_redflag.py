
from unittest import TestCase
from flask import json
from api import app

class Tests(TestCase):
    """
       Class to test api
    """ 
    
    def setUp(self):
        self.app = app
        self.client = self.app.test_client
 

    def test_get_record(self):
        """
           method to get a specific item
        """
        get_result = self.client().get('/record/1')
        self.assertEqual(get_result.status_code, 200)

    
    def test_get_records(self):
        """
           method to get all products
        """
        get_result = self.client().get('/record')
        response = json.loads(get_result.data.decode("utf8"))
        self.assertEqual(get_result.status_code, 200)
        self.assertIsInstance(response, dict)


    # def test_get_non_item(self) :  
    #     """
    #        method to test an item that does not exist
    #     """
    #     get_result = self.client().get('/record/100')
    #     self.assertEqual(get_result.status_code, 404)


    
    def test_add_record(self):
        """
           method to add a specific product
        """  
        post_result = self.client().post('/record', content_type='application/json',
                                         data=json.dumps(dict(                                         
                                            createdOn= "11/11/2011",
                                            createdBy="1111201",
                                            type= "cfgv",
                                            location= [9,8],
                                            comment= "fcgvbhj",        
                                            status= "99999")))
 
        
        print(post_result.data)
        self.assertEqual(post_result.status_code, 201)   
        json_data = json.loads(post_result.data)      
        assert json_data['status'] == 201
        assert json_data['data'][0] == {"id": 1,"message": "created red-flag record"}
        
    
   