from django.urls import path,include
from test_form_handle import views

urlpatterns = [
    path('',views.html_form_data_manual,name='test_manual_link'),
    path('django_form/',views.django_form,name= 'django_form_link')
]

