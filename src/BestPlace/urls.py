from django.urls import path
from django.contrib import admin
from django.conf.urls import include, url
urlpatterns = [
    path('', include("parkingGenie.urls")),
    url(r"^admin/", admin.site.urls),
]

