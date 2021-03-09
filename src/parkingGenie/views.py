from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the landing page for parking lot genie.")