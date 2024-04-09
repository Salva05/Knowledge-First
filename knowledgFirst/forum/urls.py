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
    path('delete_topic/<int:id>', views.delete_topic, name='delete_topic'),
    path('delete_reply/', views.delete_reply, name='delete_reply'),
    path('post_like/<int:post_id>/', views.post_like, name='post_like'),
    path('reply_like/<int:reply_id>/', views.reply_like, name='reply_like'),
    path('discussions/', views.discussions, name='discussions'),
    path('update_post', views.update_post, name='update_post'),
    path('member/<int:profile_id>', views.member, name='member'),
    path('follow/<int:profile_id>/', views.follow_user, name='follow_user'),
    path('unfollow/<int:profile_id>/', views.unfollow_user, name='unfollow_user'),
]