from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View


class IndexView(View):
    def get(self, request):
        return HttpResponse("<h1> Výtejte na stránkách naší autopůjčovny <h1/>"
                            "<a href='http://localhost:8000/katalog/seznam/'>Jaká máme k dispozici auta?</a>"
                            "<h2> O náší půjčovně: <h2/> <br>"
                            "<p> Naše autopůjčovna vznikla v roce 2019 a na truhu je přes 30 let<p/>")
class SeznamView(View):
    def get(self, request):
        return HttpResponse("<ul>"
 " <li>Skoda Oktávia</li>"
 " <li>Peugeot</li> "
 " <li> Mercedes</li>"
 " <li> Maserati </li>"
"</ul>")