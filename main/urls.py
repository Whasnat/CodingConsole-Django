from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'main-home'),
    path('login', views.login, name = 'login'),
    path('about/', views.about, name = 'main-about'),

]