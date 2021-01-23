from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import static


urlpatterns=[
    url(r'^$',views.home,name='home'),


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)