# -*- coding: utf-8 -*-
""" 
    Author: luckyxiang
    @Time:2019/05/16-19:55
"""
from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', LinkView.as_view(), name='link')
]