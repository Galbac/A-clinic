from django.shortcuts import render
from rest_framework import viewsets

from .models import Doctor, Service, Appointment, Review
from .serializers import ReviewSerializer, AppointmentSerializer, ServiceSerializer, DoctorSerializer


# Create your views here.

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

def home(request):
    return render(request, 'clinic/index.html')