from django.urls import path

from . import views

urlpatterns = [
    path('', views.KontakyView.as_view(), name='index'),
    path("organizace/", views.OrganizaceView.as_view(), name = "organizace")
]