from django.urls import path
from . import views

app_name = "parkingGenie"

urlpatterns = [
    path('', views.index, name='index')
]