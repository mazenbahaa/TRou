from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('driver', views.driver, name='driver'),
    path('logins', views.logins, name='logins'),
    path('registers', views.registers, name='registers'),
    path('report', views.report, name='report'),
    path('request', views.request, name='request'),
    path('ride', views.ride, name='ride'),
    path('user', views.user, name='user'),
    path('vehicle', views.vehicle, name='vehicle'),
    path('AddRide', views.AddRide, name='AddRide'),
    path('AddDriver', views.AddDriver, name='AddDriver'),
    path('AddReport', views.AddReport, name='AddReport'),
    path('AddRequest', views.AddRequest, name='AddRequest'),
    path('AddVehicle', views.AddVehicle, name='AddVehicle'),
    

    #API URL Section
	path('Ride-list/', views.rideList, name="Ride-list"),
	path('Ride-detail/<str:pk>/', views.rideDetail, name="Ride-detail"),
	path('Ride-create/', views.rideCreate, name="Ride-create"),
	path('Ride-update/<str:pk>/', views.rideUpdate, name="Ride-update"),
	path('Ride-delete/<str:pk>/', views.rideDelete, name="Ride-delete"),
]