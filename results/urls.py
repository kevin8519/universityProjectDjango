'''
Created on Aug 14, 2016

@author: KEVIN
'''
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from results import views, viewslog
from results.views import Greeting, Studentcreate, Studentlist, StudentDetail, DeleteStudent, StudentUpdate, Markcreate


urlpatterns = [
    

    url(r'^index/studentregister/$', views.display),                    
    url(r'^index/$', views.index),                     
    url(r'^display/(?P<id>[\d+]{1})/$', views.display_projectweb),                                           
    url(r'^greeting/$', Greeting.as_view(), name='greeting'),
    url(r'^index1/student_registration/$', views.registrationstudent),
    url(r'^index1/$', views.index1),
    url(r'^stureg/$', views.stureg,name='stureg' ),
    url(r'^stureg/student_registrationclass/$', Studentcreate.as_view(), name='studentcreate'),
    url(r'^stureg/student_list/$',login_required(Studentlist.as_view()), name='studentlist'), 
    url(r'^stureg/studentdetail/(?P<pk>\d+)/$', login_required(StudentDetail.as_view(template_name='studentdetail.html')), name='studentdetail'),  
    url(r'^stureg/deletestudent/(?P<id>\d+)/$', login_required(DeleteStudent.as_view()), name='delete_student'),  
    url(r'^stureg/StudentUpdate/(?P<id>\d+)/$', StudentUpdate.as_view(), name='studentUpdate'),                 
    url(r'^stureg/results/createmarks/$', login_required(Markcreate.as_view()), name='Markcreate'),
     
    url(r'^contact/$', views.contactus, name='contactus'),
    url(r'^test/$', viewslog.test, name='test'),
    url(r'^cookie_demo/$', viewslog.cookie_demo, name='cookie_demo'),
    
    
    

       
]
