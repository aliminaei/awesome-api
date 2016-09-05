from django.conf.urls import url
from django.contrib import admin
from api import views

urlpatterns = [
    # url('/', views.schema_view),
    url(r'^users/$', views.ListCreateUserView.as_view()),
    url(r'^users/(?P<username>[\w-]+)/$', views.UserDetail.as_view()),
]
