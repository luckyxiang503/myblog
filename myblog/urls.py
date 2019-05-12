"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, converters

# from blog.views import post_detail, post_list
from blog.views import IndexView, CategoryView, TagView, PostDetailView
from config.views import links


urlpatterns = [
    # path('', post_list, name='index'),
    # re_path(r'^category/(?P<category_id>\d+)/$', post_list, name='category_list'),
    # re_path(r'^tag/(?P<tag_id>\d+)/$', post_list, name='tag_list'),
    # re_path(r'^post/(?P<post_id>\d+).html$', post_detail, name='post_detail'),
    # re_path(r'^links/$', links, name='links'),

    # 使用class views
    path('', IndexView.as_view(), name='index'),
    re_path(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category_list'),
    re_path(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag_list'),
    re_path(r'^post/(?P<post_id>\d+).html$', PostDetailView.as_view(), name='post_detail'),
    re_path(r'^links/$', links, name='links'),

    path('admin/', admin.site.urls),
]
