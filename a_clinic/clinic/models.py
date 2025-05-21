from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
user = get_user_model()


class Doctor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    slug = models.SlugField(unique=True, blank=True, verbose_name='URL')
    specialization = models.CharField(max_length=100, verbose_name='Специализация')
    photo = models.ImageField(upload_to='doctors/', verbose_name='Фото', null=True, blank=True)
    bio = models.TextField(verbose_name='Биография')
    experience_years = models.PositiveIntegerField(default=0, verbose_name='Стаж (в годах)')
    education = models.TextField(verbose_name='Образование', blank=True)
    price_per_consultation = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена за приём',
                                                 null=True, blank=True)
    rating = models.FloatField(default=0, verbose_name='Рейтинг')
    special_services = models.TextField(verbose_name='Специальные услуги', blank=True)
    seo_description = models.CharField(max_length=160, verbose_name='SEO описание', blank=True)
    accepts_online = models.BooleanField(default=False, verbose_name='Онлайн-консультации')
    appointments_url = models.URLField(verbose_name='Ссылка на запись', null=True, blank=True)
    video_presentation = models.URLField(verbose_name='Видео-презентация', null=True, blank=True)
    working_days = models.CharField(max_length=100, verbose_name='Рабочие дни', blank=True)
    working_hours = models.CharField(max_length=100, verbose_name='Рабочие часы', blank=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Мужской'), ('female', 'Женский')], verbose_name='Пол',
                              blank=True)
    available = models.BooleanField(default=True, verbose_name='Доступен')
    social_links = models.ForeignKey('SocialNetwork', on_delete=models.SET_NULL, null=True, blank=True,
                                     verbose_name='Соц. сети')

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'

    def __str__(self):
        return f"{self.name} ({self.specialization})"

    def get_absolute_url(self):
        return reverse('doctor_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название услуги')
    description = models.TextField(verbose_name='Описание')
    icon = models.CharField(verbose_name='Иконка', null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name


class FAQ(models.Model):
    question = models.CharField(verbose_name='Вопрос')
    answer = models.CharField(verbose_name='Ответ')

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = 'FAQ'


class Appointment(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя пациента', null=True)
    email = models.EmailField(verbose_name='E-mail', null=True)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона', null=True)
    date = models.DateTimeField(verbose_name='Дата', null=True)
    department = models.ForeignKey("Departments", on_delete=models.CASCADE, verbose_name='Отдел', null=True)
    doctor = models.ForeignKey("Doctor", on_delete=models.CASCADE, verbose_name='Врач', null=True)
    message = models.TextField(blank=True, verbose_name='Сообщение', null=True)

    def __str__(self):
        return f"{self.name} — {self.date.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name = 'Запись на прием'
        verbose_name_plural = 'Записи на прием'


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


class Departments(models.Model):
    name = models.CharField(verbose_name='Название отделения')
    bio = models.CharField(verbose_name="Краткое описание")
    photo = models.ImageField(verbose_name="Фото", upload_to='departments/', blank=True, null=True)
    description = models.CharField(verbose_name="Описание")

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return f'{self.name}'


class SocialNetwork(models.Model):
    name = models.CharField(blank=True, null=True, verbose_name='Имя')
    instagram = models.URLField(blank=True, null=True, verbose_name='Instagram')
    whatsapp = models.URLField(blank=True, null=True, verbose_name='Whatsapp')
    telegram = models.URLField(blank=True, null=True, verbose_name="Telegram")

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'

    def __str__(self):
        return f"Соцсети: Instagram={self.instagram}, Telegram={self.telegram}, WhatsApp={self.whatsapp}"


# class Menu(models.Model):
# name = models.CharField(verbose_name='Название клиники')
# number = models.CharField(verbose_name='Номер телефона')
# email = models.EmailField(verbose_name="E-mail")
# appointment = models.CharField(verbose_name='Записаться на прием')
# social_links = models.OneToOneField('SocialNetwork', on_delete=models.SET_NULL, null=True, blank=True)


class Title(models.Model):
    name = models.CharField(verbose_name='Название заголовка')
    description = models.CharField(verbose_name='Описание')
