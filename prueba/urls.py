from django.contrib import admin
from django.urls import path

from prueba.views.studient_view import index
urlpatterns = [
    path('studient/',index,name='index')
]