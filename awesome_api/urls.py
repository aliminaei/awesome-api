from django.conf.urls import url, include
from django.contrib import admin
from api import views

urlpatterns = [
    url(r'^', include('api.urls')),
    url(r'^admin/', admin.site.urls),
]
