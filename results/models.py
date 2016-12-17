from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    age=models.IntegerField()
    M=1
    F=2
    GENDER=(
            
            (M,'Male'),
            (F,'Female'),
            
            
            )
    gender=models.IntegerField(choices=GENDER,default=M)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    
    def __str__(self):
        
        return str(self.id)+'-'+ self.name
    
class Marks(models.Model): 
    studentmark=models.ForeignKey(Student,on_delete=models.CASCADE)  
    ENGLISH=1
    MATHS=2
    PHYSICS=3
    SUBJECTS=(
              
            (ENGLISH,'english'),  
             (MATHS,'maths'), 
             (PHYSICS,'physics'),  
               
               
              
              ) 
    subject=models.IntegerField(choices=SUBJECTS)
    marks=models.IntegerField()