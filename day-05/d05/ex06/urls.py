from django.urls import path
from . import views

urlpatterns = [
    path('init/', views.create_table),
    path('populate/', views.populate),
    path('display/', views.display),
    path('update/', views.update),
]
