


from django.contrib import admin
from django.urls import path,include



#media file packages
from django.conf import settings
from django.conf.urls.static import static

from products import views

""" 
nahian
123
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Authentication.urls')),
    path('product/',include('products.urls')),
    path('boostrapView/',views.templateView.as_view(),name='template_view_link'),

    path('search/',include('Search_engine.urls'))

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
