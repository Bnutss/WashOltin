from django.db import models
from employees.models import Employees


class Services(models.Model):
    name_services = models.CharField(max_length=200, verbose_name='Название услуги', unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена услуги')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.name_services

    class Meta:
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'
        ordering = ['-time_create', 'name_services']


class WashOrders(models.Model):
    car_name = models.CharField(max_length=255, verbose_name='Название машины')
    car_number = models.CharField(max_length=255, verbose_name='Номер авто')
    car_owner_name = models.CharField(max_length=255, verbose_name='Имя владельца авто')
    type_of_car_wash = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name='Вид мойки')
    employees = models.ForeignKey(Employees, on_delete=models.CASCADE, verbose_name='Автомойщик')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.car_name

    class Meta:
        verbose_name = 'Заказ на мойку'
        verbose_name_plural = 'Заказы на мойку'
        ordering = ['-time_create', 'car_name']
