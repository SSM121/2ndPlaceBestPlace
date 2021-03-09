from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the web site landing page. Currently nothing here :(.")