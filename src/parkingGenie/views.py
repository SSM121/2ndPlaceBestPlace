from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Event
from django.contrib import messages
from qr_code.qrcode.utils import QRCodeOptions


def index(request):
    return render(request, 'parkingGenie/index.html')


def logIn(request):
    if request.method == "POST":
        email = request.POST.get('userName')
        password = request.POST.get("userPassword")
        userName = request.POST.get("userName")
        user = authenticate(request, username=userName, password=password)
        if user is not None:  # found a pair of matching credentials
            request.session['userEmail'] = user.email
            request.session['userName'] = user.username
            request.session["password"] = password


            # type_obj = userType.objects.get(user=user) # Used to redirect the different user types
            if user.is_authenticated:
                return redirect('parkingGenie:dashBoard')
        else:  # no matching credentials
            messages.add_message(request, messages.ERROR, "Username or Password are incorrect")
            return render(request, 'parkingGenie/login.html')
    elif request.method == "GET":
        return render(request, 'parkingGenie/login.html')


def register(request):
    errors = 0
    if request.method == "POST":
        userName = request.POST.get('userName')

        if User.objects.filter(username=userName).exists():
            messages.add_message(request, messages.ERROR, "Username is already in use")
            errors += 1

        password1 = request.POST.get("userPassword1")
        password2 = request.POST.get("userPassword2")
        userEmail = request.POST.get("userEmail")

        if User.objects.filter(email=userEmail).exists():
            messages.add_message(request, messages.ERROR, "Email is already in use")
            errors += 1

        userFirst = request.POST.get("userFirst")
        userLast = request.POST.get("userLast")
        deals = request.POST.get("deals")

        if password1 != password2:
            messages.add_message(request, messages.ERROR, 'Passwords do not match')
            errors += 1

        if request.POST.get("userType") == "Select":
            messages.add_message(request, messages.ERROR, 'Must select a user type')
            errors += 1
        if errors > 0:
            return render(request, 'parkingGenie/register.html')
        else:
            user = User.objects.create_user(userName, userEmail, password1)
            user.username = userName
            user.name = userFirst + " " + userLast
            # Set session tokens
            request.session['userEmail'] = user.email
            request.session['userName'] = user.username
            request.session['name'] = user.name
            user.profile.userType = request.POST.get("userType")  # Adds additional info to the user using forms
            user.save()
            return redirect('parkingGenie:dashBoard')  # send the new user to the dash board

    elif request.method == "GET":
        return render(request, 'parkingGenie/register.html')


def forgotUser(request):
    return render(request, 'parkingGenie/forgotUser.html')


def forgotPassword(request):
    return render(request, 'parkingGenie/forgotPassword.html')


def dashBoard(request):
    return render(request, 'parkingGenie/dashBoard.html')


def manageAccount(request):
    user = authenticate(request, username=request.session.get("userName"), password=request.session.get("password"))
    context = {
        "userType": user.profile.userType,
        "userEmail": request.session.get("userEmail"),
        "userName": request.session.get("userName"),
    }
    return render(request, 'parkingGenie/manageAccount.html', context=context)


def addEvent(request):
    return render(request, 'parkingGenie/addEvent.html')


def addLot(request):
    return render(request, 'parkingGenie/addLot.html')


def searchEvents(request):
    # hear we will get info from the database but for now it will be poplulated with some dummy info
    # events should be put in the dictionary form:
    # {
    #   id: number
    #   name: string
    #   date: date represented as a string
    #   startTime: time as a string
    # }
    eventList = Event.objects.order_by('date')
    context = {
        'eventList': eventList,
    }
    return render(request, 'parkingGenie/events.html', context)


def lotSearch(request, event_id):
    #dictionary for storing event info
    # should get from the event_id but for now just the info besides the id is just dummy values
    eventInfo = {
        "id": event_id,
        "name": "USU Vs SDSU",
        "date": "Oct. 19, 2021",
        "startTime": "3:00 p.m."
    }
    # list of lot dictionaries
    lotList = []
    # should get lots for event given from database. for now dummy values are used
    # dictionaries should have the form
    # {
    #   lotID: int #this is the id within the event itself
    #   openSpots: int
    #   address: string
    #   price: int
    #   hasTailGate: bool
    #   distance in miles: int
    # }
    lotList.append({
        "lotID": 0,
        "openSpots": 69,
        "address": "dummy address 1",
        "price": 20,
        "hasTailGate": True,
        "distance": 4
    })
    lotList.append({
        "lotID": 1,
        "openSpots": 420,
        "address": "dummy address 2",
        "price": 10,
        "hasTailGate": False,
        "distance": 1
    })
    lotList.append({
        "lotID": 2,
        "openSpots": 42,
        "address": "dummy address 3",
        "price": 25,
        "hasTailGate": True,
        "distance": 5
    })
    context = {
        "eventInfo": eventInfo,
        "lotList": lotList
    }
    return render(request, 'parkingGenie/lotSearch.html', context)


def qrViewer(request):
    # Build context for rendering QR codes.
    context = {
        "my_options": QRCodeOptions(size='m', border=0, error_correction='s'),
        "qrCode": "http://127.0.0.1:8000/qrViewer",  # Will need to be replaced with dynamic QR code generator
        "userName": request.session.get("userName")
    }

    # Render the view
    return render(request, 'parkingGenie/qrViewer.html', context)


def checkOut(request):
    lotID = request.GET.get("lot")
    eventName = request.GET.get("event")
    context = {
        "lotId": lotID,
        "eventName": eventName,  # I think this will needed be substituted later with an event ID
    }
    return render(request, 'parkingGenie/checkOut.html', context)

