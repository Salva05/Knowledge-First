from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('elenco', views.elenco, name='elenco'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('list/<str:type>', views.specific_list, name='specific_list'),
    path('search', views.search, name='search'),
    path('signup/', views.signup, name='signup'),
    path('signup_success/', views.signup_success, name='signup_success'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('profile/', views.profile, name='profile'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('required_signin/', views.required_signin, name='required_signin'),
    path('submit_reply/', views.submit_reply, name='submit_reply'),
]