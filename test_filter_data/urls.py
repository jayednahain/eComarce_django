from django.urls import path,include
from test_filter_data import views

urlpatterns = [
    path('',views.data_show,name='login_link'),

]

