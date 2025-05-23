# Generated by Django 5.2.1 on 2025-05-20 09:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0008_alter_faq_options_service_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('whatsapp', models.URLField(blank=True, null=True, verbose_name='Whatsapp')),
                ('telegram', models.URLField(blank=True, null=True, verbose_name='Telegram')),
            ],
            options={
                'verbose_name': 'Социальная сеть',
                'verbose_name_plural': 'Социальные сети',
            },
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='social_network_instagram',
        ),
        migrations.AddField(
            model_name='doctor',
            name='social_links',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clinic.socialnetwork'),
        ),
    ]
