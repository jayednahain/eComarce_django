


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
    path('',include('test_form_handle.urls')),
    path('authentication/',include('test_authentication.urls')),
    # path('product/',include('products.urls'))

    #class based veiw
    path('product_list_CB/',views.CB_ProductListview.as_view()),
    path('product_detail_CB/<int:pk>', views.CB_ProductDetailview.as_view(),name='CB_detail_link'),

    #featured view
    path('product_featured_list_CB/',views.CB_FeaturedListView.as_view()),
    path('product_featured_detail_CB/<int:pk>',views.CB_FeaturedDetailView.as_view(),name='CB_featured_deatil'),

    #function based view
    path('product_list_FB/',views.FB_productListView),
    path('product_detail_FB/<int:pk>',views.FB_ProductDetailview,name='FB_detail_link'),

    #slugView
    path('product_slug_detail_CB/<str:slug>',views.Slug_productDetailView.as_view(),name='CB_featured_deatil'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
