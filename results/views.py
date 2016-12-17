from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, \
    PermissionRequiredMixin
from django.contrib.syndication.views import Feed
from django.db import connection
from django.http.response import HttpResponse
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.utils.decorators import method_decorator
from django.utils.feedgenerator import Atom1Feed
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from results.forms import Studentform, Markform 
from results.models import Student, Marks


# Create your views here.
def dear(request):
    
    return HttpResponse('welcome to django kevin'+request.META['HTTP_USER_AGENT'])



def display(request):
    name=request.GET['name']
    city=request.GET['city']
    age=request.GET['age']
    phone=request.GET['phone']
    email=request.GET['email']
    
    sql="INSERT INTO projectweb.webproject (name, city, age, phone, email) VALUES ('"+name+"','"+city+"','"+age+"','"+phone+"','"+email+"') "
    print(name,city,age,phone,email)
    print sql
    cursor=connection.cursor()
    cursor.execute(sql)
    return HttpResponse(" form uploaded done")


def display_projectweb(request,id):
    sql="select name, city, age, phone, email from webproject where id='"+id+"' "
    cursor=connection.cursor()
    cursor.execute(sql)
    result=cursor.fetchall()
    my_html=''
    for r in result:
        print r
        print my_html
        my_html="<html><head><style>body {background-color: powderblue;}th,td{color:red;}</style></head><body><table border=3><tr><th><label>Name</label></th><td>"+r[0]+"</td></tr><tr><th><label>City</label></th><td>"+r[1]+"</td></tr><tr><th><label>Age</label></th><td>"+str(r[2])+"</td></tr><tr><th><label>Phone</label></th><td>"+str(r[3])+"</td> </tr><tr><th><label>Email</label></th><td>"+r[4]+"</td></tr></table> </body></html>"                                                                                                     
                   
    return HttpResponse(my_html)    
def index(request):
    template='my_form.html'
    data={
    }
    return render_to_response(template,data,RequestContext(request))


def index1(request):
    template='student_registration.html'
    data={'student_form': Studentform() }
    
    return render(request,template,data) 
 
 
 
@login_required    
def registrationstudent(request): 
    
    
    student=Student()  
    student.name=request.POST['name']
    student.city=request.POST['city']
    student.age=request.POST['age']
    student.gender=request.POST['gender']
    student.address=request.POST['address']
    student.phone=request.POST['phone']
    student.save()
    
    return HttpResponse('User successfully registered')   
        
class Greeting(View):
    
    greet='hi man how are you'
    
    
    def get(self,request):
        
        return HttpResponse(self.greet) 
    
@login_required
def index2(request):
    template='welcome.html'
    data={}
    
    return render(request,template,data) 

def searh(request):
    template='search.html'
    data={}
    
    return render(request,template,data) 



@login_required
def stureg(request):
    template='student_registrationclass.html'
    data={'student_form': Studentform() }
    
    return render(request,template,data) 

class Studentcreate(LoginRequiredMixin,CreateView): 
    
    model=Student 
    success_url='/welcome/stureg/student_list/'    
    form_class=Studentform  
  
class Studentlist(PermissionRequiredMixin,ListView): 
    model=Student
    context_object_name='student_list'        
    template_name='student_list.html'
    permission_required='results.change_student'
   
class StudentDetail(DetailView):  
    model=Student 
    #template_name='student_list.html' 
   
class DeleteStudent(DeleteView):  
    model=Student  
    success_url='/welcome/stureg/student_list/'
    
    def get_object(self, queryset=None):
        
        obj=Student.objects.get(id=self.kwargs['id'])
        return obj
  
class StudentUpdate(UpdateView): 
    model=Student
    success_url='/welcome/stureg/student_list/'    
    form_class=Studentform    
    
    def get_object(self, queryset=None):
        
        obj=Student.objects.get(id=self.kwargs['id'])
        return obj 
    
 
class Markcreate(CreateView): 
    
    model=Marks 
    success_url='/welcome/stureg/results/createmarks/'    
    form_class=Markform  
    
def ajaxstudentresults(request): 
    
    if request.is_ajax():
        querry_string=request.GET.get('search_text')
        
        if querry_string is not None:
            results=Marks.objects.filter(studentmark_id=querry_string).order_by('subject')
            try:
                studentmark=Student.objects.get(pk=querry_string)
                studentmark=studentmark.name
                
            except:
                
                studentmark=''
                
            template='results/student_results.html'
            data={
                  
                  'results':results,
                  'student_name':studentmark
                
                  }    
                    
            return render_to_response(template, data, RequestContext(request))
    
def contactus(request):
    
    
    template='contactus.html'
    data={}
    return render(request,template,data) 
    
    
    
       
    