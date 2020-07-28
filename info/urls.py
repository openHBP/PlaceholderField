# encoding:utf-8
'''
Created on 13/04/2020
@author: p.houben
'''
from django.urls import path
from info.views import voir

app_name = "info"

urlpatterns = [
    path('accueil', voir, name='accueil'),
]
