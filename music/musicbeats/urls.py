from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('songs/', views.songs, name='songs'),
    path('songs/<int:id>', views.songpost, name='songpost'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
]