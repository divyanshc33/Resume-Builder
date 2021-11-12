from django.shortcuts import render, redirect
from django.contrib.auth.models import User 

# Create your views here.
def register(request):

   # user = User.objects.create_user('fname', 'username', 'email', 'password', 'repeatPassword')
   return render(request, 'users/Register.html')


def login(request):
   if request.method=="POST":
      username == request.POST.get('username')
      password == request.POST.get('password')

      #check if user has entered correct credentials
      User = authenticate(username='username', password='password')

      if User is not None:
         return redirect("/")
      else:
         return render(request, 'users/Login.html')

   return render(request, 'users/Login.html')