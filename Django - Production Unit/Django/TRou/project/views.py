from multiprocessing import context
from django.shortcuts import redirect, render

from .forms import *
from .models import *

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import RideSerializer


def dashboard(request):
    # dict x= {'name':'ali'}
    return render(request, 'pages/dashboard.html')


def driver(request):
    drivers = users.objects.all()
    context = {'drivers': drivers}
    return render(request, 'pages/driver.html', context)


def logins(request):
    return render(request, 'pages/logins.html')


def registers(request):
    return render(request, 'pages/registers.html')


def report(request):
    mark = Reports.objects.all()
    context = {'mark': mark}
    return render(request, 'pages/report.html', context)


def request(request):
    mark = Requests.objects.all()
    context = {'mark': mark}
    return render(request, 'pages/request.html', context)


def ride(request):
    CarRoutes = Routes.objects.all()
    context = {'CarRoutes': CarRoutes}
    return render(request, 'pages/ride.html', context)


def user(request):
    return render(request, 'pages/user.html')


def vehicle(request):
    mark = Vehicles.objects.all()
    context = {'mark': mark}
    return render(request, 'pages/vehicle.html', context)


def AddRide(request):
    form = ARideForm()
    if request.method == 'POST':
        form = ARideForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/ride')

    context = {'form': form}
    return render(request, 'pages/ARide.html', context)


def AddDriver(request):
    form = ADriverForm()
    if request.method == 'POST':
        form = ADriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/driver')

    context = {'form': form}
    return render(request, 'pages/ADriver.html', context)


def AddReport(request):
    form = AReportForm()
    if request.method == 'POST':
        form = AReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/report')

    context = {'form': form}
    return render(request, 'pages/AReport.html', context)


def AddRequest(request):
    form = ARequestForm()
    if request.method == 'POST':
        form = ARequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/request')

    context = {'form': form}
    return render(request, 'pages/ARequest.html', context)


def AddVehicle(request):
    form = AVehicleForm()
    if request.method == 'POST':
        form = AVehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/vehicle')

    context = {'form': form}
    return render(request, 'pages/AVehicle.html', context)


def Add(request):

    context = {}
    return render(request, 'pages/Add.html', context)


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