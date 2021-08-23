from django.shortcuts import render
from .forms import ContactForm
# Create your views here.


def html_form_data_manual(request):
   if request.method == "POST":
      name=request.POST.get('name')
      email = request.POST.get('email')
      password = request.POST.get('password')
      print(name)



   return render(request,'manual_form_data.html')



"""tradional away"""
# def django_form(request):
#    form = ContactForm()
#
#    if request.method == "POST":
#       full_name = request.POST.get('full_name')
#       email = request.POST.get('email')
#       content = request.POST.get('content')
#       print(full_name)
#       print(content)
#    return render(request,'djangoform.html',{'form':form})


"""passing request method though Form perameter"""
# def django_form(request):
#    form = ContactForm(request.POST or None)
#    full_name = request.POST.get('full_name')
#    email = request.POST.get('email')
#    content = request.POST.get('content')
#    print(full_name)
#    print(content)
#    return render(request,'djangoform.html',{'form':form})

            #"""Using claned data"""
# def django_form(request):
#
#    form = ContactForm(request.POST or None)
#    full_name = request.POST.get('full_name')
#    email = request.POST.get('email')
#    content = request.POST.get('content')
#    print(full_name)
#    print(content)
#    if form.is_valid():
#       #after submit if the data is still on the field
#       print(form.cleaned_data)
#    return render(request,'djangoform.html',{'form':form})

"""using custom field error """ # error used in forms.py file
def django_form(request):
   form = ContactForm(request.POST or None)
   full_name = request.POST.get('full_name')
   email = request.POST.get('email')
   content = request.POST.get('content')
   print(full_name)
   print(content)
   if form.is_valid():
      # after submit if the data is still on the field
      print(form.cleaned_data)
   return render(request, 'djangoform.html', {'form': form})
