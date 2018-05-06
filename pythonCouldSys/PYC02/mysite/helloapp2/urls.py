# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     urls
   Description :
   Author :       XWH
   date：          2018/2/8
-------------------------------------------------
   Change Activity:
                   2018/2/8:
-------------------------------------------------
"""
__author__ = 'XWH'

from django.urls import path
from . import views

urlpatterns = [
    path('',views.hello)
]