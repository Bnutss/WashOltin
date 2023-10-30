from django.db import models
from datetime import date


class Positions(models.Model):
    name_positions = models.CharField(max_length=100, verbose_name='Название должности', unique=True)
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.name_positions

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        ordering = ['-time_update', 'name_positions']


class Employees(models.Model):
    GENDER_CHOICES = [
        ('Мужской', 'Мужской'),
        ('Женский', 'Женский'),
    ]
    FIRED_CHOICES = [
        (True, 'Да'),
        (False, 'Нет'),
    ]
    name_employees = models.CharField(max_length=255, verbose_name='ФИО', unique=True)
    position = models.ForeignKey(Positions, on_delete=models.CASCADE, verbose_name='Должность')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name='Пол')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    address = models.TextField(blank=True, verbose_name='Адрес проживания')
    hire_date = models.DateField(null=True, blank=True, verbose_name='Дата приёма на работу')
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Оклад')
    pinfl = models.CharField(max_length=14, verbose_name='ПИНФЛ')
    passport_number = models.CharField(max_length=50, verbose_name='Серия и № паспорта')
    passport_issued_by = models.CharField(max_length=200, verbose_name='Кем выдан паспорт')
    passport_issued_date = models.DateField(null=True, blank=True, verbose_name='Дата выдачи паспорта')
    fired = models.BooleanField(null=False, verbose_name='Статус увольнения')
    date_of_termination = models.DateField(null=True, blank=True, verbose_name='Дата увольнения')
    default_photo_path = 'employees_photos/default.png'
    photo = models.ImageField(upload_to='employees_photos/', null=True, blank=True, verbose_name='Фото',
                              default=default_photo_path)
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def save(self, *args, **kwargs):
        if self.fired and not self.date_of_termination:
            self.date_of_termination = date.today()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_employees

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['-time_create', 'name_employees', 'fired']
