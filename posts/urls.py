# posts/urls.py
from django.urls import path , re_path
from django.conf.urls import url
from .views import PostListView, PostDetailView
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    # path('<slug:slug>', PostDetailView.as_view(), name='post_detail'),
    url('add/post/$' , views.add_post , name='add_post'),
    url('edit/(?P<slug>[-\w]+)/' , views.edit_post, name = 'edit_post'),

    re_path(r'^(?P<slug>[-\w]+)/', PostDetailView.as_view(), name='post_detail'),
    path('', PostListView.as_view(), name='post_list'),
    # url(r'^edit/post/(?P<id>\d+)$' , views.edit_post, name = 'edit_post'),
    ]
    #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
