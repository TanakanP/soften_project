from django.conf.urls import url,include
from django.contrib import admin

from main import views

urlpatterns = [
    url(r'^$',views.home , name='home'),
    url(r'^product/',views.product , name='product'),
]