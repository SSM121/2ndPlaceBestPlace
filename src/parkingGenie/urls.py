from django.urls import path
from . import views

app_name = "parkingGenie"

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.logIn, name='login'),
    path('register', views.register, name='register'),
    path('addEvent', views.addEvent, name='addEvent'),
    path('addLot', views.addLot, name='addLot'),
    path('events', views.searchEvents, name='searchEvents'),
    path('event/<int:event_id>', views.lotSearch, name='lotSearch'),

]