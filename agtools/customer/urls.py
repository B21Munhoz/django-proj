from django.urls import path
from customer.views import CustomerTemplateView, CustomerFormTemplateView


app_name = 'customers'

urlpatterns = [
    path('', CustomerTemplateView.as_view(), name='customers'),
    path('create/', CustomerFormTemplateView.as_view(), name='create'),
]
