from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render

from django.conf import settings
import random

from .forms import signUpForm, logInForm
from django.contrib import auth
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User


def main(request):
    data = {}

    # if not request.COOKIES.get('username'):
    if not request.user.is_authenticated:
        user = settings.USER_NAMES[random.randrange(9)]

        request.COOKIES['username'] = user
        response = render(request, 'ex01/main_page.html', data)
        response.set_cookie('username', user, max_age=42)
    else:
        data['logged_in'] = 'True'
        response = render(request, 'ex01/main_page.html', data)
    
    return response

def signup(request):
    data = {}

    if request.user.is_authenticated:
        return render(request, 'ex01/main_page.html', data)

    if request.method == 'POST':
        form = signUpForm(request.POST)
        data['form'] = form

        if form.is_valid():
            if request.POST['password'] == request.POST['confirm_password']:
                try:
                    user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
                    user.save()
                    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
                    if user is None:
                        data['error'] = f"Error. Cannot authenticate user {request.POST['username']}. Please try again"
                    else:
                        auth_login(request, user)
                        request.COOKIES['username'] = request.POST['username']
                        data['logged_in'] = 'True'
                        response = render(request, 'ex01/main_page.html', data)
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

def login(request):
    data = {}

    if request.user.is_authenticated:
        data['logged_in'] = 'True'
        return render(request, 'ex01/main_page.html', data)

    if request.method == 'POST':
        try:
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user is None:
                data['error'] = f"Error. Cannot authenticate user {request.POST['username']}. Please try again"
            else:
                auth_login(request, user)
                request.COOKIES['username'] = request.POST['username']
                data['logged_in'] = 'True'
                response = render(request, 'ex01/main_page.html', data)
                response.set_cookie('username', request.POST['username'], max_age=31536000) # 1 year
                return response
        except Exception:
            return HttpResponse(Exception)
    
    form = logInForm
    data['form'] = form
    return render(request, 'ex01/login.html', data)

def logout(request):
    try:
        auth_logout(request)
    except Exception:
        pass
    return main(request)