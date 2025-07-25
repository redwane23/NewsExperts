# Generated by Django 3.2.25 on 2025-06-27 23:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import home.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities_light', '0011_alter_city_country_alter_city_region_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(blank=True, max_length=100)),
                ('LastName', models.CharField(blank=True, max_length=100)),
                ('Email', models.EmailField(blank=True, max_length=254)),
                ('Picture', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('date_of_search', models.CharField(choices=[('yesterday', 'yesterday'), ('last week', 'last week'), ('last mounth', 'last mounth')], default='yesterday', max_length=20)),
                ('City', models.ForeignKey(blank=True, default=home.models.default_country, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='City', to='cities_light.city')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
