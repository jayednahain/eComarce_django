from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from products.models import Porduct
from django.db.models import Q


class CB_Search_ProductListview(ListView):
   template_name = 'search_result_view.html'
   #traditional away
   # def get_context_data(self,*args, **kwargs):
   #    context = super(CB_Search_ProductListview, self).get_context_data(*args, **kwargs)
   #    context['query'] = self.request.GET.get('q')

   def get_queryset(self,*args,**kwargs):
      request = self.request
      print(request.GET)
      q = request.GET.get('search_data')
      if q is not None:
         return Porduct.objects.search_data(q)
      return Porduct.objects.featured()


