from django.shortcuts import render
from django.views.generic import DetailView, CreateView, TemplateView
from rest_framework import viewsets

from .models import Doctor, Service, Appointment, Review, Testimonial
from .serializers import DoctorSerializer, ServiceSerializer, AppointmentSerializer, ReviewSerializer
from .templates.clinic.utils import send_telegram_message


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


from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import AppointmentForm, TestimonialForm
from .models import Doctor, FAQ, Departments, Service


class HomeView(FormView):
    template_name = 'clinic/index.html'
    form_class = AppointmentForm
    success_url = reverse_lazy('appointment_success')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        doctors = Doctor.objects.filter(available=True)
        context['faq'] = FAQ.objects.all()
        context['departments'] = Departments.objects.all()
        context['services'] = Service.objects.all()
        context['grouped_doctors'] = list(zip(*[iter(doctors)] * 4, strict=False))
        context['testimonials'] = Testimonial.objects.order_by('-date')
        context['testimonial_form'] = TestimonialForm()
        return context

    def form_invalid(self, form):
        # Возвращаем форму с нужным контекстом (врачи, услуги и т.д.)
        context = self.get_context_data(form=form)
        return render(self.request, self.template_name, context)

    def form_valid(self, form):
        appointment = form.save()
        # Отправка в Telegram
        send_telegram_message(appointment)

        return super().form_valid(form)


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
        print("Форма валидна!", form.cleaned_data)  # Проверяем, вызывается ли этот метод
        appointment = form.save()
        send_telegram_message(appointment)
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Форма невалидна!", form.errors)  # Смотрим ошибки
        return super().form_invalid(form)


class TestimonialCreateView(CreateView):
    model = Testimonial
    form_class = TestimonialForm
    template_name = 'clinic/testimonial_form.html'
    success_url = reverse_lazy('home')


class TestimonialsView(TemplateView):
    template_name = "clinic/testimonials_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        doctor = Doctor.objects.get(slug=slug)
        context["doctor"] = doctor
        context["testimonials"] = Testimonial.objects.filter(doctor=doctor)
        return context


class TestimonialsAllView(TemplateView):
    template_name = "clinic/testimonials_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["testimonials"] = Testimonial.objects.order_by('-date')
        return context
