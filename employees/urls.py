from django.urls import path
from employees.views import (
    EmployeesListView,
    ViewEmployeesView,
    EmployeesSearchView
)

app_name = 'employees'

urlpatterns = [
    path('employees-list/', EmployeesListView.as_view(), name='employees_list'),
    path('view-employees/<int:employees_id>/', ViewEmployeesView.as_view(), name='view_employees'),
    path('employees-search/', EmployeesSearchView.as_view(), name='employees_search'),
]
