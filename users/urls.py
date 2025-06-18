# users/urls.py

from django.urls import path
from .views import LoginAPI, LoginAPI2, AddCustomerAPI, CustomerListAPI

urlpatterns = [
    path('login/', LoginAPI2.as_view(), name='login'),
    path('add-customer/', AddCustomerAPI.as_view(), name='add_customer'),
    path('all-customers/', CustomerListAPI.as_view(), name='all_customers')
]
