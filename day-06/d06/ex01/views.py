from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render

from django.conf import settings
import random

from .forms import signUpForm, logInForm
from django.contrib import auth
from django.contrib.auth.models import User


def main(request):
    response = render(request, 'ex01/main_page.html')

    if not request.COOKIES.get('username'):
        user = settings.USER_NAMES[random.randrange(9)]

        request.COOKIES['username'] = user
        response = render(request, 'ex01/main_page.html')
        response.set_cookie('username', user, max_age=42)
    
    return response

def signup(request):
    data = {}

    if request.user.is_authenticated:
        return render(request, 'ex01/main_page.html')

    if request.method == 'POST':
        form = signUpForm(request.POST)
        data['form'] = form

        if form.is_valid():
            if request.POST['password'] == request.POST['confirm_password']:
                try:
                    user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
                    user.save()
                    login(request, user)
                    user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
                    if user is None:
                        return HttpResponse(f"Error. Cannot authenticate user {request.POST['username']}")
                    login(request, user)
                    request.COOKIES['username'] = request.POST['username']
                    response = render(request, 'ex01/main_page.html')
                    response.set_cookie('username', request.POST['username'], max_age=31536000) # 1 year
                    return response
                except Exception:
                    data['error'] = 'Error. Username is already in use. Please choose another one'
            else:
                data['error'] = 'Error. Passwords are not equal'
        else:
            data['error'] = 'Error. Passwords are not equal'
        
        return render(request, 'ex01/signup.html', data)

    form = signUpForm
    data['form'] = form
    return render(request, 'ex01/signup.html', data)
    return HttpResponse("signup page")

def login(request):
    data = {}

    if request.method == 'POST':
        return HttpResponse("login post method")
    
    form = logInForm
    data['form'] = form
    return render(request, 'ex01/login.html', data)
    return HttpResponse("login page")