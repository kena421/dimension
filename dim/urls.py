
from django.conf.urls import url,path
from django.contrib import admin

urlpatterns = [
    url('', admin.site.urls),
    url('', include(portal.urls)),
]
