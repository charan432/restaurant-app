# Generated by Django 3.0.1 on 2019-12-18 13:30

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('street', models.CharField(blank=True, max_length=100, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('city', models.CharField(default='', max_length=20)),
                ('zipCode', models.CharField(blank=True, max_length=20, null=True)),
                ('stateOrProvince', models.CharField(blank=True, max_length=20, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('telephone', models.CharField(blank=True, max_length=20, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
