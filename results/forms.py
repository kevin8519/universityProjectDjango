'''
Created on Aug 19, 2016

@author: KEVIN
'''
from django import forms
from django.contrib.auth.models import User
from django.forms.models import ModelForm

from results.models import Student, Marks


class Studentform(ModelForm):
   name=forms.CharField(widget=forms.TextInput(attrs={'style':'border:1px dotted #000000;'})) 
   address=forms.CharField(widget=forms.TextInput(attrs={'style':'border:3px inset #FF2256'}))
    
   class Meta:
        
        model=Student
        
        fields='__all__'
        #fields=( 'name', 'address','age')
class Markform(ModelForm):
   
    
   class Meta:
        
        model=Marks
        
        fields='__all__'
        #fields=( 'name', 'address','age')  
        
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField(
                        widget=forms.TextInput(attrs={'class': "input"}),)
    class Meta:
        model = User
        fields = ('username', 'email', 'password')        
          