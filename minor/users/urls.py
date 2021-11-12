from django.urls import path
from . import views
from users import views
urlpatterns = [
    path('Login', views.login, name='users-Login'),
    path('Register', views.register, name='users-Register'),
]