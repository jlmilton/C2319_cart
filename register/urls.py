from . import views
from .views import profile
from django.urls import path, re_path
from django.conf.urls import url


urlpatterns = [
    # url(r'^$', views.home),
    url(r'^profile/$', views.profile, name="profile"),
]
