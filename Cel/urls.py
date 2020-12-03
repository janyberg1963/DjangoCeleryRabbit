from django.urls import path
from . import views

urlpatterns = [
    path('', views.Post_Celery, name='post_celery')

]

