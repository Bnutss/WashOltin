from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from .forms import WashOrdersForm
from employees.models import Employees
from django.core.paginator import Paginator
from .models import WashOrders
from decimal import Decimal


class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        return render(request, 'login.html', {"login_form": login_form})

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect("carwash:main_menu")
        else:
            error_message = "Неверный логин или пароль."
            messages.error(request, error_message)
            return render(request, 'login.html', {"login_form": login_form})


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect("carwash:login")


class MainMenuView(LoginRequiredMixin, View):
    template_name = 'main_menu.html'

    @method_decorator(login_required, name='dispatch')
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name)


class AddOrdersView(LoginRequiredMixin, View):
    template_name = 'add_order.html'

    def get(self, request):
        form = WashOrdersForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = WashOrdersForm(request.POST, request.FILES)
        if form.is_valid():
            model = form.save(commit=False)
            model.firms = form.cleaned_data['car_name']
            model.save()
            form.save_m2m()
            return redirect('carwash:main_menu')
        return render(request, self.template_name, {'form': form})


class TotalListView(LoginRequiredMixin, View):
    template_name = 'total_for_today.html'
    item_page = 20

    def get(self, request):
        employees_with_orders = Employees.objects.filter(washorders__isnull=False).distinct()
        paginator = Paginator(employees_with_orders, self.item_page)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)
        employee_data = []

        for employee in page:
            carwash_data = WashOrders.objects.filter(employees=employee)
            total_cars_washed = carwash_data.count()
            total_amount = carwash_data.aggregate(Sum('type_of_car_wash__price'))['type_of_car_wash__price__sum']
            total_amount = Decimal(total_amount)
            commission_percentage = Decimal("0.3")
            commission = total_amount * commission_percentage
            net_earnings = total_amount - commission
            employee_data.append({
                'employee': employee,
                'total_cars_washed': total_cars_washed,
                'total_amount': total_amount,
                'commission': commission,
                'net_earnings': net_earnings,
            })

        return render(request, self.template_name, {'page': page, 'employee_data': employee_data})
