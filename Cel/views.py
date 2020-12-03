
from django.shortcuts import render, redirect
from django_celery_results.models import TaskResult
from django.contrib.auth.models import User
from django.utils import timezone
from .tasks import add
from celery import Celery

# Create your views here.

def Post_Celery(request):
    a=add.delay(2,2)
    
    


    stuff_for_frontend = {'a': a}
        
    return render(request, 'Cel/Celery_base.html',stuff_for_frontend)

