from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$',views.cart_detail , name='cart_detail'),
    url(r'^add/(?P<product_id>[-\w]+)$', views.cart_add, name='cart_add'),
    url(r'^sub/(?P<product_id>[-\w]+)$', views.cart_sub, name='cart_sub'),
    url(r'^remove/(?P<product_p>[-\w]+)/$', views.cart_remove, name='cart_remove'),
]
