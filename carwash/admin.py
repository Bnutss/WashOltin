from django.contrib import admin
from carwash.models import Services, WashOrders


class ServicesAdmin(admin.ModelAdmin):
    list_display = (
        'name_services', 'price',)
    list_display_links = ('name_services',)
    search_fields = ('name_services',)


class WashOrdersAdmin(admin.ModelAdmin):
    list_display = ('employees', 'type_of_car_wash', 'car_owner_name', 'car_number', 'car_name', 'time_create')
    list_display_links = ('employees',)
    search_fields = ('employees',)
    list_filter = ('employees',)
    autocomplete_fields = ['employees', 'type_of_car_wash']


admin.site.register(Services, ServicesAdmin)
admin.site.register(WashOrders, WashOrdersAdmin)
