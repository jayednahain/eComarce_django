from django.shortcuts import render

# Create your views here.


def data_show(request):
   return render(request,'filter_data.html')