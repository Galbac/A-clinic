from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views
from .views import DoctorViewSet, ServiceViewSet, AppointmentViewSet, ReviewViewSet

router = SimpleRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.home, name='home')
]
