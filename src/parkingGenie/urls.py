from django.urls import path
from . import views

app_name = "parkingGenie"

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.logIn, name='login'),
    path('forgotUser', views.forgotUser, name='forgotUser'),
    path('forgotPassword', views.forgotPassword, name='forgotPassword'),
    path('register', views.register, name='register'),
    path('addEvent', views.addEvent, name='addEvent'),
    path('addLot', views.addLot, name='addLot'),
    path('dashBoard', views.dashBoard, name='dashBoard'),
    path('manageAccount', views.manageAccount, name='manageAccount'),
    path('events', views.searchEvents, name='searchEvents'),
    path('event/<int:event_id>', views.lotSearch, name='lotSearch'),
]