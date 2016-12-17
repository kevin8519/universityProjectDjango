from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client


# Create your tests here.
class TestLoggedUser(TestCase):
    
    def setup(self):
        
        self.client = Client() 
        self.user=User(username='minu', email='min@emial.com',password='minu')
        self.user.save()
        self.client.login(username='minu', password='minu') 
        
      
    def test_homepage(self): 
        response = self.client.get('/')
        print response
        self.assertEqual(response.status_code, 200)
    def test_logged_user_get_registration(self): 
        response = self.client.get('/welcome/stureg/')
        print response              
        self.assertEqual(response.status_code, 200)  
        
    def test_logged_user_get_student_list(self): 
        response = self.client.get('/welcome/stureg/student_list/')
        print response              
        self.assertEqual(response.status_code, 302) 
     
    def tearDown(self): 
        self.user.delete()       
                