from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from .models import WashOrders


class AccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class CustomPasswordChangeForm(PasswordChangeForm):
    pass


class WashOrdersForm(forms.ModelForm):
    class Meta:
        model = WashOrders
        fields = ['car_name', 'car_number', 'car_owner_name', 'type_of_car_wash', 'employees']
