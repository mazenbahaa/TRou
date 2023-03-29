from django.shortcuts import redirect, render
from django.shortcuts import render
from .forms import *
from .models import *

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import RideSerializer


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
	form = ARideForm()
	if request.method == 'POST':
		form = ARideForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/ride')

	context = {'form':form}
	return render(request, 'pages/ARide.html', context)

def AddDriver(request):
	form = ADriverForm()
	if request.method == 'POST':
		form = ADriverForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/driver')

	context = {'form':form}
	return render(request, 'pages/ADriver.html', context)    

def AReport(request):
	form = AReportForm()
	if request.method == 'POST':
		form = AReportForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/report')

	context = {'form':form}
	return render(request, 'pages/AReport.html', context)

def ARequest(request):
	form = ARequestForm()
	if request.method == 'POST':
		form = ARequestForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/request')

	context = {'form':form}
	return render(request, 'pages/ARequest.html', context) 

def AVehicle(request):
	form = AVehicleForm()
	if request.method == 'POST':
		form = AVehicleForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/request')

	context = {'form':form}
	return render(request, 'pages/AVehicle.html', context)   

def Add(request):

    context = {}
    return render(request , 'pages/Add.html', context)


# API Section:

@api_view(['GET'])
def rideList(request):
    ridesList = Routes.objects.all().order_by('-id')
    serializer = RideSerializer(ridesList, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def rideDetail(request, pk):
    ridesDetaial = Routes.objects.get(id=pk)
    serializer = RideSerializer(ridesDetaial, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def rideCreate(request):
    serializer = RideSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def rideUpdate(request, pk):
    rideUpdate = Routes.objects.get(id=pk)
    serializer = RideSerializer(instance=rideUpdate, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def rideDelete(request, pk):
    rideDelete = Routes.Objects.get(id=pk)
    rideDelete.delete()

    return Response('Item Successfully delete!')