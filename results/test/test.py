'''
Created on Sep 17, 2016

@author: KEVIN
'''
from django.contrib.auth.models import User
from django.test.client import Client
from django.test.testcases import TestCase


class TestLoggedUser(TestCase):
    
    def setup(self):
        
        self.client = Client()
        
        
        
    def test_login(self):    
        self.user=User.objects.create_user('minu', 'min@emial.com', 'minu') 
        #self.user=User(username='minu', email='min@emial.com',password='minu')
        self.user.save()
        self.client.login(username='minu',password='minu')
    
             
    def test_view_home_route(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        
    def test_logged_user_get_registration(self): 
        response = self.client.get('/welcome/stureg/')
        print response              
        self.assertEqual(response.status_code, 200)       
        
    def test_logged_user_get_student_list(self): 
        response = self.client.get('/welcome/stureg/student_list/')
        print response              
        self.assertEqual(response.status_code, 302)
    def teardown(self): 
        
        self.user.delete()  
        

    