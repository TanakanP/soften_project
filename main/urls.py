from django.conf.urls import url,include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from main import views

urlpatterns = [
    url(r'^home/',views.home , name='home'),
    url(r'^catalog/product/',views.product , name='product'),
    url(r'^catalog/',views.catalog , name='catalog'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)