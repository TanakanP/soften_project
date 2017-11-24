from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.models import User
from django.conf import settings
from django.conf.urls.static import static
from main import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),

    url(r'^underconstruction/', views.underconstruction, name='underconstruction'),
    url(r'^contact/', views.contact, name='contact'),

    url(r'^product/$', views.product, name='productnull'),
    url(r'^product/(?P<product_id>.+)/$', views.product, name='product'),

    url(r'^account/$', views.account, name='accountnull'),
    url(r'^account/(?P<username>.+)/$', views.account, name='account'),
    url(r'^account/upload/$',views.upload_pic , name='upload_pic'),
    url(r'^history/(?P<order_id>[-\w]+)/$', views.orderdetail, name='orderdetail'),

    url(r'^news/', views.news, name='news'),
    url(r'^article/(?P<news_id>[-\w]+)/$', views.article, name='article'),
    url(r'^article/', views.article, name='article'),

    url(r'^updatePrice/', views.update, name='update'),

    url(r'^catalog/$', views.catalog, name='catalog'),
    url(r'^catalog-(?P<product_brand>.+)/$',views.catalog,{'key_sort':'name'}, name='catalog'),
    url(r'^sale/$', views.catalog, {'key_sort':'sale'},name='sale'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
