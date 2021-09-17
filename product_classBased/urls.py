from django.urls import path,include
# from products import views
from product_classBased import views

urlpatterns = [

   #product list view
   path('list_classbased/',views.ProductListView.as_view(),name='list_view_class_based_link'),
   #product list view
   path('detailview_classe_Based/<int:pk>',views.DetailViewProduct.as_view(),name='detail_view_classed_link')
]



