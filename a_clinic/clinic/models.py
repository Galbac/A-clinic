from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
user = get_user_model()


class Doctor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    specialization = models.CharField(max_length=100, verbose_name='Специализация')
    photo = models.ImageField(upload_to='doctors/', verbose_name='Фото', null=True, blank=True)
    bio = models.TextField(verbose_name='Биография')
    available = models.BooleanField(default=True, verbose_name='Доступен')
    social_network_instagram = models.CharField(blank=True, verbose_name='Инстаграм')

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'

    def __str__(self):
        return f"{self.name} ({self.specialization}, {self.available}, {self.photo})"


class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название услуги')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='Врач')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Услуга')
    date = models.DateTimeField(verbose_name='Дата и время')
    comment = models.TextField(blank=True, verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Запись на прием'
        verbose_name_plural = 'Записи на прием'

    def __str__(self):
        return f"{self.user.username} - {self.doctor.name} ({self.date})"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='Врач')
    text = models.TextField(verbose_name='Текст отзыва')
    rating = models.PositiveSmallIntegerField(default=5, verbose_name='Рейтинг')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f"Отзыв от {self.user.username} - {self.rating}/5"
