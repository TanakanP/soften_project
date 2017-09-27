from django.conf.urls import url,include
from django.contrib import admin

from payment import views

urlpatterns = [
    url(r'^$',views.checkout , name='checkout'),
]
