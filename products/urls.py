
from django.urls import path

from products import views


urlpatterns = [
    #class based veiw
    path('product_list_CB/',views.CB_ProductListview.as_view(),name='CB_list_link'),

    #slugView
    path('product_slug_detail_CB/<str:slug>',views.Slug_productDetailView.as_view(),name='CB_slug_deatil'),

]


"""

    path('product_detail_CB/<int:pk>', views.CB_ProductDetailview.as_view(),name='CB_detail_link'),
    
    #featured view
    path('product_featured_list_CB/',views.CB_FeaturedListView.as_view()),
    path('product_featured_detail_CB/<int:pk>',views.CB_FeaturedDetailView.as_view(),name='CB_featured_deatil'),
    
    
    
    #function based view
    path('product_list_FB/',views.FB_productListView),
    path('product_detail_FB/<int:pk>',views.FB_ProductDetailview,name='FB_detail_link'),


"""