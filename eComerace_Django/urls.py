


from django.contrib import admin
from django.urls import path,include



#media file packages
from django.conf import settings
from django.conf.urls.static import static
#7.1
from products import views
from cart_user.views import cart_view

""" 
nahian
123
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Authentication.urls')),
    path('product/',include('products.urls')),
    path('boostrapView/',views.templateView.as_view(),name='template_view_link'),

    path('search/',include('Search_engine.urls')),

    path('cart/',cart_view,name='cart_link')


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
