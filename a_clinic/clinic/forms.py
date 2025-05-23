from django import forms
from django.utils.timezone import is_naive, make_aware, now
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

from .models import Appointment, Testimonial, Departments


class AppointmentForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox, required=True,
                             error_messages={'required': 'Пожалуйста, подтвердите, что вы не робот.'})

    class Meta:
        model = Appointment
        fields = ['name', 'email', 'phone', 'date', 'department', 'message', 'captcha']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ваш Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш телефон'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'doctor': forms.Select(attrs={'class': 'form-select'}),
            'message': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Сообщение (необязательно)', 'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].empty_label = "Выберите отделение"
        self.fields['department'].queryset = Departments.objects.all()

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and not phone.isdigit():
            raise forms.ValidationError('Телефон должен содержать только цифры.')
        if phone and len(phone) < 10:
            raise forms.ValidationError('Телефон слишком короткий.')
        return phone

    def clean_date(self):
        date = self.cleaned_data['date']
        if is_naive(date):
            date = make_aware(date)
        if date < now():
            raise forms.ValidationError('Дата не может быть в прошлом.')
        return date

    def clean_captcha(self):
        captcha_value = self.cleaned_data.get('captcha')
        if not captcha_value:
            raise forms.ValidationError("Пожалуйста, подтвердите, что вы не робот.")
        return captcha_value

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name and len(name) < 2:
            raise forms.ValidationError('Имя должно содержать не менее 2 символов.')
        return name


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'doctor', 'department', 'stars', 'text', 'image']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4}),
        }