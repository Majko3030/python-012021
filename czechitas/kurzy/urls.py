from django.urls import path

from . import views

urlpatterns = [
    path('', views.KurzyView.as_view(), name='index_kurzy'),
path('<int:pk>', views.DetailKurzView.as_view(), name='detail_kurzu'),
path('prihlaska/', views.VytvorPrihlasku.as_view(), name='prihlaska'),
path('prihlaska/potvrzeni/', views.PotvrzeniPrihlasky.as_view(), name='potvrzeni_prihlasky'),
]
# nahrazením KurzyView lze změnit pohled
#druhá cesta - aby ukldáalo hodnotu kurzu a následně, int:pk - co vloží do tatabáze - dostane
#číslo - 1. kurz 1, 2. kurz č.2... - to bude primární klíč