from django.http.response import HttpResponse
from django.shortcuts import render

from django.conf import settings
import random

from .forms import signUpForm, logInForm


def main(request):
    response = render(request, 'ex01/main_page.html')

    if not request.COOKIES.get('username'):
        user = settings.USER_NAMES[random.randrange(9)]

        request.COOKIES['username'] = user
        response = render(request, 'ex01/main_page.html')
        response.set_cookie('username', user, max_age=42)
    
    return response

def signup(request):
    form = signUpForm
    data = {'form' : form}
    return render(request, 'ex01/signup.html', data)
    return HttpResponse("signup page")

def login(request):
    form = logInForm
    data = {'form' : form}
    return render(request, 'ex01/login.html', data)
    return HttpResponse("login page")