from django.urls import path,include
from products import views

urlpatterns = [

   #product list view
   path('list_classbased/',views.ProductListView.as_view(),name='list_view_class_based_link'),
   path('list_functionbased/',views.productList,name='list_function_based_link'),


   #product list view
   path('detailview_classe_Based/<int:pk>',views.DetailViewProduct.as_view(),name='detail_view_classed_link'),
   path('detailview_function_based/<int:pk>',views.productdetail,name='detail_view_function_link')
]



