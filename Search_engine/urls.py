
from django.urls import path

from Search_engine import views


urlpatterns = [
    #class based veiw
    path('',views.CB_Search_ProductListview.as_view(),name='search_link'),


]
