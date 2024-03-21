from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('elenco', views.elenco, name='elenco'),
    path('dettaglio/<int:id>', views.dettaglio, name='dettaglio'),
]