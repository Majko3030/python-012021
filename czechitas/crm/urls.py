from django.urls import path

from . import views

urlpatterns = [
    path('', views.PrvniPohled.as_view(), name='index'),
]