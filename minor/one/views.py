from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'one/home.html')

def Login(request):
   return render(request, 'one/Login.html')

