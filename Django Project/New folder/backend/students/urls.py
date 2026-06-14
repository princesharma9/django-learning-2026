
from sys import path
 
from . import views
from django.urls import path
urlpatterns = [
    path('api/',views.students, name='students'),
]
