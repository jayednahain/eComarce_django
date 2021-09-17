from django.urls import path,include
from product_functionBased import views

urlpatterns = [

   #product list view
   path('list_functionbased/',views.productList,name='list_function_based_link'),


   #product list view
   path('detailview_function_based/<int:pk>',views.productdetail,name='detail_view_function_link')
]



