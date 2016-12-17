'''
Created on Sep 2, 2016

@author: KEVIN
'''
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from results.forms import UserForm

def test(request):
    
    return HttpResponse("i am a boy")



def user_login(request):
    
    if request.user.is_authenticated():
        template='welcome.html'
        data={}
        return render(request,template,data)   
    if request.method =='POST' :
        
        username=request.POST['username']
        password=request.POST['password']
        
        user=authenticate(username=username,password=password)
        
        if user:
            
            if user.is_active:
                login(request,user)
                template='welcome.html'
                data={'user':user}
                return render(request,template,data) 
            
            else:
                return HttpResponse("Your account disabled")
                
        else:        
            print "invalid login{0}, {1} details provided" .format(username,password)
                
            
            template='login.html'
            data={"response":"Invalid Login Credentials!!"}
            return render (request,template,data)
            
    else:
        
        template='login.html'
        data={}
        return render (request,template,data) 
    
    
    
    
def logout_view(request):
    
    logout(request) 
    return redirect('login')



def register(request):
    # Like before, get the request's context.
    #context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render(request,
            'register.html',
            {'user_form': user_form, 'registered': registered})

def cookie_demo(request):
  
    if 'name' in request.COOKIES:
        cookie_id = request.COOKIES['city']
        return HttpResponse('Got cookie with id=%s' % cookie_id)
    else:
        resp = HttpResponse('No id cookie! Sending cookie to client')
        resp.set_cookie('name', "Kevin")
        resp.set_cookie('age', "28")
        resp.set_cookie('city', "USA")
        return resp   
def test_count_session(request):
    if 'count' in request.session:
        request.session['count'] += 1
        return HttpResponse('new count=%s' % request.session['count'])
    else:
        request.session['count'] = 1
        return HttpResponse('No count in session. Setting to 1')
    
    
            