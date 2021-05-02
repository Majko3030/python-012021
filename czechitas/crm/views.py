from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView
from . import models


class PrvniPohled(View):
    def get(self, request):
        return HttpResponse('Vítej v CRM systému Czechitas!')

class KontakyView(ListView):
    model = models.Kontakt
    template_name = "crm_list.html"
# odkazuje template_name - na složku template v aplikaci

class OrganizaceView(ListView):
    model = models.Organizace
    template_name = "organizace_list.html"

class Detail_organizace (DetailView):
    model= models.Organizace
    template_name = "organizace_detail.html"
