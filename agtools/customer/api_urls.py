from django.urls import path
from customer.views import CustomerAPIView


app_name = 'api_customers'

urlpatterns = [
    path('', CustomerAPIView.as_view(), name='customers'),
]
