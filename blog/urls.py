# -*- coding: utf-8 -*-
""" 
    Author: luckyxiang
    @Time:2019/05/16-19:53
"""
from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    re_path(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category_list'),
    re_path(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag_list'),
    re_path(r'^post/(?P<post_id>\d+).html$', PostDetailView.as_view(), name='post_detail'),
    re_path(r'^search/$', SearchView.as_view(), name='search'),
    path('create_post', CreatePostView.as_view(), name='create_post')
]