


from django.contrib import admin
from django.urls import path,include


""" 
nahian
123
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('test_form_handle.urls')),
    path('authentication/',include('test_authentication.urls'))
]
