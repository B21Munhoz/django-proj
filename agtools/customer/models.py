from django.db import models

# Create your models here.
class Customer(models.Model):
    full_name = models.CharField('Nome', max_length=150, blank=False)
    email = models.EmailField(blank=False, unique=True)


def get_all_customers():
    return Customer.objects.order_by('full_name')
