from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from user_authentication.views import LoginTemplateView, logout_view


auth_urlpatterns = [
    path('login/', LoginTemplateView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('api/auth/', ObtainAuthToken.as_view()),
]
