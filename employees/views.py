from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Employees
from django.core.paginator import Paginator
from django.db.models import Q


class EmployeesListView(LoginRequiredMixin, View):
    template_name = 'employees/employees_list.html'
    item_page = 20

    def get(self, request):
        employees = Employees.objects.all()
        paginator = Paginator(employees, self.item_page)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)
        return render(request, self.template_name, {'page': page})


class ViewEmployeesView(LoginRequiredMixin, View):
    template_name = 'employees/view_employees.html'

    def get(self, request, employees_id):
        employees = get_object_or_404(Employees, id=employees_id)
        context = {'employee': employees}
        return render(request, self.template_name, context)


class EmployeesSearchView(LoginRequiredMixin, View):
    template_name = 'employees/employees_list.html'
    item_page = 20

    def get(self, request):
        query = request.GET.get('query')

        if query is not None:
            employees = Employees.objects.filter(
                Q(name_employees__icontains=query) | Q(pinfl__icontains=query))
        else:
            employees = Employees.objects.all()
        paginator = Paginator(employees, self.item_page)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)
        return render(request, self.template_name, {'page': page})
