from django.contrib import admin
from employees.models import Employees, Positions


class EmployeesAdmin(admin.ModelAdmin):
    list_display = (
        'name_employees', 'birth_date', 'position', 'fired', 'date_of_termination')
    list_display_links = ('name_employees',)
    search_fields = ('name_employees',)
    autocomplete_fields = ['position']


class PositionsAdmin(admin.ModelAdmin):
    list_display = ('name_positions',)
    list_display_links = ('name_positions',)
    search_fields = ('name_positions',)


admin.site.register(Employees, EmployeesAdmin)
admin.site.register(Positions, PositionsAdmin)
