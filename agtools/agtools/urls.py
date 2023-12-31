"""
URL configuration for agtools project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from user_authentication.urls import auth_urlpatterns
from agtools.views import index

urlpatterns = []

if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))

urlpatterns.extend(
    [
        path('', index, name='home'),
        path('admin/', admin.site.urls),
        path('customers/', include('customer.urls', namespace='customers')),
        path('api/customers/', include('customer.api_urls')),
    ]
)

urlpatterns.extend(auth_urlpatterns)
