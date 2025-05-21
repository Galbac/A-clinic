import requests
from django.views.generic import FormView, DetailView
from rest_framework import viewsets
from rest_framework.reverse import reverse_lazy

from .models import Doctor, Service, Appointment, Review
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


from .forms import AppointmentForm
from .models import Doctor, FAQ, Departments, Service
from django.core.mail import send_mail


class HomeView(FormView):
    template_name = 'clinic/index.html'
    form_class = AppointmentForm
    success_url = reverse_lazy('appointment_success')

    def form_invalid(self, form):
        print("Форма невалиднаааа!", form.errors)  # Смотрим ошибки
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        doctors = Doctor.objects.filter(available=True)
        context['faq'] = FAQ.objects.all()
        context['departments'] = Departments.objects.all()
        context['services'] = Service.objects.all()
        context['grouped_doctors'] = list(zip(*[iter(doctors)] * 4, strict=False))
        return context

    def form_valid(self, form):
        print("Форма валиднаааа!")
        appointment = form.save()

        # Отправка email
        send_mail(
            subject='Новая запись на прием',
            message=(
                f"📥 Новая запись на приём:\n\n"
                f"👤 Имя: {appointment.name}\n"
                f"📧 Email: {appointment.email}\n"
                f"📞 Телефон: {appointment.phone}\n"
                f"📅 Дата: {appointment.date}\n"
                f"🩺 Врач: {appointment.doctor}\n"
                f"💬 Сообщение: {appointment.message}"
            ),
            from_email=None,
            recipient_list=['zidan_2002@mail.ru'],  # Замени на свою почту
            fail_silently=False,
        )

        # Отправка в Telegram
        self.send_telegram_message(appointment)

        return super().form_valid(form)

    def send_telegram_message(self, appointment):
        BOT_TOKEN = '7561986373:AAHxKMyS5tR8-N-EDqsrp1Q_jEpQKTPfF60'  # Замени
        CHAT_ID = '430326400'  # Замени
        TEXT = (
            f"📥 Новая запись на приём:\n\n"
            f"👤 Имя: {appointment.name}\n"
            f"📧 Email: {appointment.email}\n"
            f"📞 Телефон: {appointment.phone}\n"
            f"📅 Дата: {appointment.date}\n"
            f"🩺 Врач: {appointment.doctor}\n"
            f"💬 Сообщение: {appointment.message}"
        )

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.post(url, data={'chat_id': CHAT_ID, 'text': TEXT})


class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'clinic/doctor_detail.html'
    context_object_name = 'doctor'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class AppointmentView(FormView):
    template_name = 'clinic/doctor_appointment.html'
    form_class = AppointmentForm
    success_url = reverse_lazy('appointment_success')

    def form_valid(self, form):
        print("Форма валидна!")  # Проверяем, вызывается ли этот метод
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Форма невалидна!", form.errors)  # Смотрим ошибки
        return super().form_invalid(form)
