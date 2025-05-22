from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import SimpleRouter

from . import views
from .views import DoctorViewSet, ServiceViewSet, AppointmentViewSet, ReviewViewSet, DoctorDetailView, AppointmentView, \
    TestimonialCreateView

router = SimpleRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.HomeView.as_view(), name='home'),
    path('appointment/success/', TemplateView.as_view(template_name='clinic/appointment_success.html'),
         name='appointment_success'),
    path('doctor/<slug:slug>/', DoctorDetailView.as_view(), name='doctor_detail'),
    path('appointment/doctor/<slug:slug>/', AppointmentView.as_view(), name='appointment'),
    path('add-testimonial/', TestimonialCreateView.as_view(), name='add_testimonial'),
]
