from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def index(request):
    return render(request, template_name='home.html')
