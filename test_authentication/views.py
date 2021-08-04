from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate,login

# Create your views here.




def home_authentication(request):
    return render(request,'home.html')


def login_page(request):
   form = LoginForm(request.POST or None)
   context = {
      'form': form
   }
   print("user is trying to log in")

   if form.is_valid():
      print(form.cleaned_data)

      #geting user data
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      #passing data through authenticate function
      user = authenticate(request,username=username,password=password)

      if user is not None:
         print('log in success full')
         login(request,user)
         #after login success page
         context['form'] = LoginForm()
         return redirect('home_page')
      else:
         print("error in log in")


   return render(request,'auth/login.html',context)

def register_page(request):
   form = LoginForm(request.POST or None)
   if form.is_valid():
      print(form.cleaned_data)
   return render(request,'auth/register.html')