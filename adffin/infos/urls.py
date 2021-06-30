from django.urls import path
from .views import newss,newsdate,register,addUser,addInfo,addDB

urlpatterns=[
    path('',newss,name='news'),
    path('newsdate/<int:year>',newsdate,name='newsdate'),
    path('signup/',register,name='register'),
    path('addUser/',addUser,name='addUser'),
    path('addInfo/',addInfo,name='addInfo'),
    path('addDB/', addDB, name='addDB')
]