from django.urls import path
from django.contrib.auth.views import logout_then_login
from accounts import views

urlpatterns = [
    path('send_login_email', views.send_login_email, name='send_login_email'),
    path('login', views.login, name='login'),
    path('logout', logout_then_login, name='logout_then_login'),
]