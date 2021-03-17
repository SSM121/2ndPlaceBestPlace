from django.shortcuts import render
from django.template import loader

def index(request):
    return render(request, 'parkingGenie/index.html')


def logIn(request):
    return render(request, 'parkingGenie/login.html')


def register(request):
    return render(request, 'parkingGenie/register.html')

  
def addEvent(request):
    return render(request, 'parkingGenie/addEvent.html')

  
def addLot(request):
    return render(request, 'parkingGenie/addLot.html')

