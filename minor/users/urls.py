from django.urls import path
from . import views
from users import views
urlpatterns = [
    path('Login/', views.Login, name='users-Login'),
    path('Register/', views.Register, name='users-Register'),
]