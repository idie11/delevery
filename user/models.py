from django.conf import settings
from django.db import models


class Profiles(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, models.CASCADE, related_name='user_profile', null=True)
    first_name = models.CharField('Имя', max_length=255, blank=True, null=True)
    last_name = models.CharField('Фамилия', max_length=255, blank=True, null=True)
    balance = models.PositiveIntegerField('Баланс', default=0)
    dob = models.DateField('Дата рождения', blank=True, null=True)
    

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



class Courier(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, 
        related_name='courier', null=True, unique=True
    )
    first_name = models.CharField('Имя', max_length=255, blank=True, null=True)
    last_name = models.CharField('Фамилия', max_length=255, blank=True, null=True)
    car = models.TextField('Описание машины', blank=True, null=True)

    class Meta:
        verbose_name = 'Курьер'
        verbose_name_plural = 'Курьеры'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
