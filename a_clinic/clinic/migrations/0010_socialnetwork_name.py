# Generated by Django 5.2.1 on 2025-05-20 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0009_socialnetwork_remove_doctor_social_network_instagram_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialnetwork',
            name='name',
            field=models.CharField(blank=True, null=True, verbose_name='Имя'),
        ),
    ]
