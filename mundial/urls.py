from django.urls import path
from . import views
from django.contrib.auth.views import (LoginView, LogoutView,)

urlpatterns = [
    # path('login/', views.login_page, name='login_page'),
    path('', views.start_page, name='start_page'),
    path('register/', views.register_page, name='register_page'),
    path('homepage/', views.homepage, name='homepage'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', LogoutView.as_view(), name='logout_page'),
    path('standings/', views.standings_page, name='standings_page'),
]