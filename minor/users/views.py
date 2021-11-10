from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
def Register(request):

   user = User.objects.create_user('fname', 'username', 'email', 'password', 'repeatPassword')
   return render(request, 'users/Register.html')


def Login(request):
   if request.method=="POST":
      username == request.POST.get('username')
      password == request.POST.get('password')

      #check if user has entered correct credentials
      user = authenticate(username='username', password='password')

      if user is not None:
         return redirect("/home")
      else:
         return render(request, 'users/Login.html')

   return render(request, 'users/Login.html')