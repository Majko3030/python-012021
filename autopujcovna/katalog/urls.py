from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
urlpatterns = [
    path('', views.SeznamView.as_view(), name='index'),
]