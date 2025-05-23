# Generated by Django 5.2.1 on 2025-05-21 17:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0016_alter_doctor_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='specialization',
        ),
        migrations.AddField(
            model_name='doctor',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='clinic.departments', verbose_name='Специализация'),
            preserve_default=False,
        ),
    ]
