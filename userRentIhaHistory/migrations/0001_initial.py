# Generated by Django 5.0.4 on 2024-04-20 19:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('iha', '0002_alter_iha_model'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRentIhaHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateField()),
                ('finishDate', models.DateField()),
                ('startTime', models.TimeField()),
                ('finishTime', models.TimeField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('iha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iha.iha')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
