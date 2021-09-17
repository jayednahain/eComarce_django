


from django.contrib import admin
from django.urls import path,include



#media file packages
from django.conf import settings
from django.conf.urls.static import static


""" 
nahian
123
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('test_form_handle.urls')),
    path('authentication/',include('test_authentication.urls')),
    path('filter_data/',include('test_filter_data.urls')),
    #path('product/',include('products.urls')),
    #classbased
    path('product_classbased/',include('product_classBased.urls')),

    #functionbassed
    path('product_functionbased/',include('product_functionBased.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
