# Generated by Django 5.2.1 on 2025-05-20 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0004_doctor_social_network_instagram_alter_doctor_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(verbose_name='Вопрос')),
                ('answer', models.CharField(verbose_name='Ответ')),
            ],
        ),
    ]
