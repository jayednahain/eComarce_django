from django.urls import path,include
from test_authentication import views

urlpatterns = [
    path('',views.login_page,name='login_link'),
    path('homepage/',views.home_authentication,name='home_page'),
    path('registation/',views.register_page,name='registation_page_link')
]

