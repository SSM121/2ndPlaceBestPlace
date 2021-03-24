from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404


def index(request):
    return render(request, 'parkingGenie/index.html')


def logIn(request):
    if request.method == "POST":
        userName = request.POST.get('userName')
        password = request.POST.get("userPassword")
        user = authenticate(username=userName, password=password)
        if user != None:  # found a pair of matching credentials
            request.session['userEmail'] = user.email
            request.session['userName'] = user.username
            request.session['firstName'] = user.first_name
            request.session['firstName'] = user.last_name
            return redirect('parkingGenie:dashBoard')
        else:  # no matching credentials
            return render(request, 'parkingGenie/login.html')
    elif request.method == "GET":
        return render(request, 'parkingGenie/login.html')


def register(request):
    if request.method == "POST":
        userName = request.POST.get('userName')
        password1 = request.POST.get("userPassword1")
        password2 = request.POST.get("userPassword2")
        userEmail = request.POST.get("userEmail")
        userFirst = request.POST.get("userFirst")
        userLast = request.POST.get("userLast")
        if password1 == password2:
            user = User.objects.create_user(userFirst, userEmail, password1)
            user.username = userName
            user.last_name = userLast
            # Set session tokens
            request.session['userEmail'] = user.email
            request.session['userName'] = user.username
            request.session['firstName'] = user.first_name
            request.session['firstName'] = user.last_name
            return redirect('parkingGenie:dashBoard')  # send the new user to the dash board
        else:  # passwords dont match
            return render(request, 'parkingGenie/register.html')
    elif request.method == "GET":
        return render(request, 'parkingGenie/register.html')


def forgotUser(request):
    return render(request, 'parkingGenie/forgotUser.html')


def forgotPassword(request):
    return render(request, 'parkingGenie/forgotPassword.html')


def dashBoard(request):
    return render(request, 'parkingGenie/dashBoard.html')


def manageAccount(request):
    context = {
        "userEmail": request.session.get("userEmail"),
        "userName": request.session.get("userName")
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
    eventList = []
    eventList.append({
        "id": 0,
        "name": "BYU Vs USU",
        "date": "Nov. 21, 2021",
        "startTime": "9:00 a.m."
    })
    eventList.append({
        "id": 1,
        "name": "BYU Vs USU",
        "date": "Nov. 21, 2021",
        "startTime": "9:00 a.m."
    })
    eventList.append({
        "id": 2,
        "name": "USU Vs SDSU",
        "date": "Oct. 19, 2021",
        "startTime": "3:00 p.m."
    })
    eventList.append({
        "id": 3,
        "name": "USU Vs UNlV",
        "date": "Oct. 20, 2021",
        "startTime": "3:00 p.m."
    })
    eventList.append({
        "id": 4,
        "name": "USU Vs U of U",
        "date": "Oct. 21, 2021",
        "startTime": "5:00 p.m."
    })
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
    # }
    lotList.append({
        "lotID": 0,
        "openSpots": 69,
        "address": "dummy address 1",
        "price": 20,
        "hasTailGate": True
    })
    lotList.append({
        "lotID": 1,
        "openSpots": 420,
        "address": "dummy address 2",
        "price": 20,
        "hasTailGate": False
    })
    lotList.append({
        "lotID": 2,
        "openSpots": 42,
        "address": "dummy address 3",
        "price": 25,
        "hasTailGate": True
    })
    context = {
        "eventInfo": eventInfo,
        "lotList": lotList
    }
    return render(request, 'parkingGenie/lotSearch.html', context)

