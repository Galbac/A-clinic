# Generated by Django 5.2.1 on 2025-05-23 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0021_alter_departments_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departments',
            name='bio',
            field=models.TextField(verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='departments',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название отделения'),
        ),
    ]
