from django.http import Http404
from django.shortcuts import render, get_object_or_404
from products.models import Porduct
# Create your views here.

from django.views.generic import ListView,DetailView


class ProductListView(ListView):
   queryset = Porduct.objects.all()
   template_name = 'product_list_classBased.html'

   def get_context_data(self,*args,**kwargs):
      context = super(ProductListView, self).get_context_data(*args,**kwargs)
      #print(context)

      return context







class DetailViewProduct(DetailView):
   #queryset = Porduct.objects.all()
   template_name = 'detail_view_classBased.html'
   def get_context_data(self,*args,**kwargs):
      context = super(DetailViewProduct,self).get_context_data(*args,**kwargs)
      print(context)
      return context

      # defing method for modified manager
   def get_object(self, *args, **kwargs):
      request = self.request
      pk = self.kwargs.get('pk')

      # applying get_by_id() modified method!
      instance = Porduct.objects.get_by_id(pk)
      if instance is None:
            # creating an error !
         raise Http404("product dosent exists")
      return instance

   #10
   #6:08
   #use deffult method
   def get_queryset(self,*args, **kwargs):
      request = self.request
      pk = self.kwargs.get('pk')
      instance = Porduct.objects.get_by_id(pk)
      return instance





