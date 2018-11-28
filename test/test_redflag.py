
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
    
    def test_get_record(self):
        """
           method to get a specific record
        """
        get_result = self.client().get('/api/v1/red-flags/1')
        self.assertEqual(get_result.status_code, 200)   
    
    
    
    
    def test_get_non_item(self) :  
        """
           method to test a record that does not exist
        """
        get_result = self.client().get('/api/v1/red-flags/qwer')
        self.assertEqual(get_result.status_code, 404)


    def test_delete_item(self) :  
        """
           method to test a record to be deleted
        """
        get_result = self.client().get('/api/v1/red-flags/1')
        self.assertEqual(get_result.status_code, 200)
    

    def test_delete_non_item(self) :  
        """
           method to delete a record that doesnot exxist
        """
        get_result = self.client().get('/api/v1/red-flags/delete')
        self.assertEqual(get_result.status_code, 404)
    def test_get_records(self):
        """
           method to get all records
        """
        get_result = self.client().get('/api/v1/red-flags')
        response = json.loads(get_result.data.decode("utf8"))
        self.assertEqual(get_result.status_code, 200)
        self.assertIsInstance(response, dict)

    # def test_update_record(self):
    #     """
    #        method to add a specific record
    #     """  
    #     post_result = self.client().post('api/v1/red-flags/1/jki', content_type='application/json',
    #                                      data=json.dumps(dict(                                         
    #                                         location= [100,8],
    #                                         comment= "were"  
    #                                         )))
 
        
        
    #     self.assertEqual(post_result.status_code, 201)   
    #     json_data = json.loads(post_result.data)      
    #     assert json_data['status'] == 201
    #     assert json_data['data'][0] == {"id": 1,"message": "uploaded red-flag's record"}     
    
    def test_add_record(self):
        """
           method to add a record
        """  
        post_result = self.client().post('/api/v1/red-flags', content_type='application/json',
                                         data=json.dumps(dict(                                         
                                            createdOn= "11/11/2011",
                                            createdBy="1111201",
                                            type= "cfgv",
                                            location= [9,8],
                                            comment= "fcgvbhj",        
                                            status= "99999")))
 
        
        
        self.assertEqual(post_result.status_code, 201)   
        json_data = json.loads(post_result.data)      
        assert json_data['status'] == 201
        assert json_data['data'][0] == {"id": 1,"message": "created red-flag record"}     
    
    def test_add_product_with_empty_fields(self):
        """
           method to test adding a record with empty fields
        """  
        post_result = self.client().post('/api/v1/red-flags', content_type = 'application/json',
                                         data=json.dumps(dict()))
        self.assertEqual(post_result.status_code, 400) 
    
   