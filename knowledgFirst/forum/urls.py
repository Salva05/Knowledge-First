from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('elenco', views.elenco, name='elenco'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('list/<str:type>', views.specific_list, name='specific_list'),
    path('search', views.search, name='search')
]