from django.urls import path
from . import views

app_name = "parkingGenie"

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.logIn, name='login'),
    path('register', views.register, name='register'),
    path('addLot', view.addLot, name='addLot'),
]