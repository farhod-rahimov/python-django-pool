from django.http.response import HttpResponse
from django.shortcuts import render

from django.conf import settings
import random


def main(request):
    response = render(request, 'ex00/main_page.html')

    if not request.COOKIES.get('username'):
        user = settings.USER_NAMES[random.randrange(9)]

        request.COOKIES['username'] = user
        response = render(request, 'ex00/main_page.html')
        response.set_cookie('username', user, max_age=42)
    
    return response
