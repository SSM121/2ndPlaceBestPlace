from django.shortcuts import render, redirect



def index(request):
    return render(request, 'parkingGenie/index.html')


def logIn(request):
    if request.method == "POST":
        name = request.POST
        request.session["name"] = name
        return redirect('parkingGenie:dashBoard')
    elif request.method == "GET":
        return render(request, 'parkingGenie/login.html')


def register(request):
    return render(request, 'parkingGenie/register.html')


def forgotUser(request):
    return render(request, 'parkingGenie/forgotUser.html')


def forgotPassword(request):
    return render(request, 'parkingGenie/forgotPassword.html')


def dashBoard(request):
    return render(request, 'parkingGenie/dashBoard.html')


def manageAccount(request):
    context = {
        "account": request.session.get("name")
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

