from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy

#pohled List View umí pracovat se seznamem z 1 modelu
from . import models

class MujPrvniPohled(View):
    def get(self, request):
        return HttpResponse('Vítej na webu Czechitas!')
class KurzyView(ListView):
    model = models.Kurz
    template_name = "kurzy/kurzy_list.html"
#dát seznam modelů, které má zobrazit hodnoty
#zároveň ví, jak zobrazit - to je atribut template name
#odkaz na šablonu musí být včetně cesty!
class DetailKurzView(DetailView):
    model = models.Kurz
    template_name = "kurzy/kurz_detail.html"

class VytvorPrihlasku(CreateView):
    model = models.Prihlaska
    template_name = "kurzy/prihlaska.html"
    fields = ["email", "jmeno","prijmeni", "motivace", "kurz"]
    success_url = reverse_lazy('potvrzeni_prihlasky')
# fiels - musí obsahovat hodnoty z modelu, pokud povnná položka v modelu, musí být k vyplnění
#pokud pole nechci, tak v modelu nastavit jako nepovinný atribut

class PotvrzeniPrihlasky(TemplateView):
    template_name = "potvrzeni.html"