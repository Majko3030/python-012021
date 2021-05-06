from django.urls import path

from . import views

urlpatterns = [
    path('', views.KontakyView.as_view(), name='index'),
    path("organizace/", views.OrganizaceView.as_view(), name = "organizace"),
path("<int:pk>", views.Detail_organizace.as_view(), name = "organizace_detail"),
    path("kontakt/", views.FormularKontakt.as_view(), name = "formular_kontakt")
]
