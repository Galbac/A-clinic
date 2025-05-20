from itertools import zip_longest

from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView, FormView
from rest_framework import viewsets
from rest_framework.reverse import reverse_lazy

from .forms import AppointmentForm
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


from django.views.generic import TemplateView
from .forms import AppointmentForm
from .models import Doctor, FAQ, Departments, Service
from itertools import zip_longest
from django.core.mail import send_mail
from django.conf import settings

class HomeView(TemplateView):
    template_name = 'clinic/index.html'

    def get(self, request, *args, **kwargs):
        doctors = Doctor.objects.filter(available=True)
        faq = FAQ.objects.all()
        departments = Departments.objects.all()
        services = Service.objects.all()
        form = AppointmentForm()

        return render(request, self.template_name, {
            'form': form,
            'faq': faq,
            'departments': departments,
            'services': services,
            'grouped_doctors': list(zip(*[iter(doctors)] * 4, strict=False))
        })

    def post(self, request, *args, **kwargs):
        form = AppointmentForm(request.POST)
        doctors = Doctor.objects.filter(available=True)
        faq = FAQ.objects.all()
        departments = Departments.objects.all()
        services = Service.objects.all()

        if form.is_valid():
            appointment = form.save()

            # Отправка email
            send_mail(
                subject='Новая запись на прием',
                message=f"Имя: {appointment.name}\n"
                        f"Email: {appointment.email}\n"
                        f"Телефон: {appointment.phone}\n"
                        f"Дата: {appointment.date}\n"
                        f"Врач: {appointment.doctor}\n"
                        f"Сообщение: {appointment.message}",
                from_email=None,
                recipient_list=['your@mail.ru'],  # Замени на свою почту
                fail_silently=False,
            )

            return redirect('appointment_success')

        # Если форма с ошибками (например, капча), возвращаем форму с ошибками
        return render(request, self.template_name, {
            'form': form,
            'faq': faq,
            'departments': departments,
            'services': services,
            'grouped_doctors': list(zip(*[iter(doctors)] * 4, strict=False))
        })



class AppointmentView(FormView):
    template_name = 'clinic/appointment.html'
    form_class = AppointmentForm
    success_url = reverse_lazy('appointment_success')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
