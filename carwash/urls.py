from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import LoginView, LogoutView, MainMenuView, AddOrdersView, TotalListView

app_name = 'carwash'

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('main-menu/', login_required(MainMenuView.as_view()), name='main_menu'),
    path('add-orders/', AddOrdersView.as_view(), name='add_orders'),
    path('total-list/', TotalListView.as_view(), name='total_list'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
