# Generated by Django 3.2 on 2021-04-29 13:15

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
            name='Stuff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Фамилия')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_stuff', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Фамилия')),
                ('balance', models.PositiveIntegerField(default=0, verbose_name='Баланс')),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Фамилия')),
                ('car', models.TextField(blank=True, null=True, verbose_name='Описание машины')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courier', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Курьер',
                'verbose_name_plural': 'Курьеры',
            },
        ),
    ]
