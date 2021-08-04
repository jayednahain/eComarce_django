from django.shortcuts import render
from .forms import LoginForm
# Create your views here.




# def home_authentication(request):
#    return render(request,'')


def login_page(request):
   form = LoginForm(request.POST or None)
   context = {
      'form':form
   }
   #print(request.user.is_authenticated())
   if form.is_valid():
      print(form.cleaned_data)

   return render(request,'auth/login.html',context)

def register_page(request):
   form = LoginForm(request.POST or None)
   if form.is_valid():
      print(form.cleaned_data)
   return render(request,'auth/register.html')