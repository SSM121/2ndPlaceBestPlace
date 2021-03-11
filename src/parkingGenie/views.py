from django.shortcuts import render


def index(request):
    return render(request, 'parkingGenie/index.html')


def logIn(request):
    return render(request, 'parkingGenie/login.html')


def register(request):
    return render(request, 'parkingGenie/register.html')
