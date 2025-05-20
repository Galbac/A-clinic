from itertools import zip_longest

from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets

from .models import Doctor, Service, Appointment, Review, FAQ, Departments
from .serializers import DoctorSerializer, ServiceSerializer, AppointmentSerializer, ReviewSerializer


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


class HomeView(TemplateView):
    template_name = 'clinic/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        doctors = Doctor.objects.filter(available=True)
        faq = FAQ.objects.all()
        departments = Departments.objects.all()
        # Группируем по 4, если не кратно 4 — дополняем None
        grouped_doctors = list(zip_longest(*[iter(doctors)] * 4, fillvalue=None))
        context['grouped_doctors'] = grouped_doctors
        context['faq'] = faq
        context['departments'] = departments
        return context


def departments(request):
    departments = Departments.objects.all()
    return render(request, "clinic/departments.html", context= {"departments": departments})
