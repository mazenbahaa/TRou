from django.shortcuts import render

# Create your views here.

def dashboard(request):
    #dict x= {'name':'ali'}
    return render(request, 'pages/dashboard.html')


def driver(request):
    return render(request, 'pages/driver.html') 


def logins(request):
    return render(request, 'pages/logins.html')                    


def registers(request):
    return render(request, 'pages/registers.html')


def report(request):
    return render(request, 'pages/report.html')             


def request(request):
    return render(request, 'pages/request.html')             


def ride(request):
    return render(request, 'pages/ride.html')   



def user(request):
    return render(request, 'pages/user.html')                    


def vehicle(request):
    return render(request, 'pages/vehicle.html') 

def ARide(request):
    return render(request, 'pages/ARide.html') 

def ADriver(request):
    return render(request, 'pages/ADriver.html')    

def AReport(request):
    return render(request, 'pages/AReport.html')

def ARequest(request):
    return render(request, 'pages/ARequest.html') 

def AVehicle(request):
    return render(request, 'pages/AVehicle.html')   
