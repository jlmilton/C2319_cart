# posts/urls.py
from django.urls import path
from django.conf.urls import url
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    path('<slug:slug>', PostDetailView.as_view(), name='post_detail'),
    path('', PostListView.as_view(), name='post_list'),
    url(r'^add/post/$' , views.add_post , name='add_post'),
    url(r'^edit/post/<slug:slug>' , views.edit_post, name = 'edit_post'),
    ]
