from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from .models import Porduct

# Create your views here.




#======================product list view

def productList(request):
   queryset = Porduct.objects.all()

   context = {
      'object_list':queryset
   }
   return render(request,'product_list_functionBasedView.html',context)


class ProductListView(ListView):
   queryset = Porduct.objects.all()
   template_name = 'product_list_classBased.html'

   def get_context_data(self,*args,**kwargs):
      context = super(ProductListView, self).get_context_data(*args,**kwargs)
      #print(context)

      return context


#======================single product viw


class DetailViewProduct(DetailView):
   queryset = Porduct.objects.all()
   template_name = 'detail_view_classBased.html'
   def get_context_data(self,*args,**kwargs):
      context = super(DetailViewProduct,self).get_context_data(*args,**kwargs)
      print(context)
      return context



def productdetail(request,pk):
   #queryset = Porduct.objects.get(pk=pk)
   instance = get_object_or_404(Porduct,pk=pk)
   print(instance.title)

   context = {
      'object': instance
   }
   return render(request,'detail_view_funsctionBasssed.html',context)