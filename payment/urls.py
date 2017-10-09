from django.conf.urls import url,include
from django.contrib import admin

from payment import views

urlpatterns = [
    url(r'^(?P<product_id>[0-9]+)$',views.checkout , name='checkout'),
]
