from django.contrib import admin
from customer.models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['email', 'full_name']


admin.site.register(Customer, CustomerAdmin)
