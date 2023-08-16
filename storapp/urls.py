from .views import display_customers, display_orders, add_new_customer, add_new_item, login_form
from django.urls import path

urlpatterns= [
    path('customers/', display_customers, name='customers'),
    path('orders/', display_orders, name='orders'),
    path('forms/',add_new_customer, name='forms'),
    path('items/',add_new_item, name = 'items'),
    path('login/', login_form, name = 'login')
]