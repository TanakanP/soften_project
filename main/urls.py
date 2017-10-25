from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.models import User
from django.conf import settings
from django.conf.urls.static import static
from main import views

urlpatterns = [
    url(r'^underconstruction/', views.underconstruction, name='underconstruction'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^home/', views.home, name='home'),
    url(r'^product/(?P<product_id>[0-9]+)/$', views.product, name='product'),
    url(r'^product/$', views.productnull, name='productnull'),
    url(r'^account/upload/$',views.upload_pic , name='upload_pic'),
    url(r'^account/(?P<username>[-\w]+)/$', views.account, name='account'),
    url(r'^account/$', views.accountnull, name='accountnull'),
    url(r'^catalog/$', views.catalog, name='catalog'),
    url(r'^catalog-(?P<product_brand>[A-z ]*)/$',views.catalog, name='catalog'),
    url(r'^catalog-(?P<product_gender>[A-z ]*)/$',views.catalog, name='catalog')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
