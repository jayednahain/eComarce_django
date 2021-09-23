from django.shortcuts import render,get_object_or_404
from django.http import Http404

from .models import Porduct
from django.views.generic import ListView,DetailView,TemplateView
from products.models import Porduct

# Create your views here.


"""only testing boostrap views !"""
class templateView(TemplateView):
   template_name = 'Bootstrap/Boostrap_base.html'





#6
#class based view
class CB_ProductListview(ListView):
   #queryset = Porduct.objects.all()
   template_name = 'class_based_views/CB_list.html'

   # def get_context_data(self,*args,**kwargs):
   #    context = super(CB_ProductListview,self).get_context_data(*args,**kwargs)
   #    #context carries every that class based view send to template
   #    return context

   #11 retrive value with get_queryset
   def get_queryset(self,*args,**kwargs):
      request = self.request
      return Porduct.objects.all()


class CB_ProductDetailview(DetailView):
   queryset = Porduct.objects.all()
   template_name = 'class_based_views/CB_detail.html'

   def get_context_data(self,*args,**kwargs):
      context = super(CB_ProductDetailview,self).get_context_data(*args,**kwargs)
      #context carries every that class based view send to template
      return context

   #11
   #using custom manager
   def get_object(self,*args,**kwargs):
      request = self.request
      pk = self.kwargs.get('pk')
      instance = Porduct.objects.get_by_id(pk)
      if instance is None:
         raise Http404('no product found from CB view ')
      return instance

   #2 get_queryset
   # def get_queryset(self, *args, **kwargs):
   #    request = self.request
   #    pk = self.kwargs.get('pk')
   #    return Porduct.objects.filter(pk=pk)


"""################# Featured CB based view###########################"""


#11
#Featured
#this view will only show those product which Featured is True or enable
class CB_FeaturedListView(ListView):
   template_name = 'featured_view/CB_FeaturedListView.html'

   def get_queryset(self, *args, **kwargs):
      request = self.request
      return Porduct.objects.all().featured()


class CB_FeaturedDetailView(DetailView):
   queryset = Porduct.objects.all().featured()
   template_name = 'featured_view/CB_FeaturedDetailView.html'

   # def get_queryset(self, *args, **kwargs):
   #    request = self.request
   #    return Porduct.objects.featured()


"""################# slug_field link use###########################"""

#12
#detail with slug link
class Slug_productDetailView(DetailView):
   template_name = 'slug_CB_detail_view/CB_slug_detailView.html'
   queryset = Porduct.objects.all()

   def get_object(self,*args,**kwargs):
      request = self.request
      slug = self.kwargs.get('slug')
      #instance = Porduct.objects.get_by_id('slug')
      #instance = get_object_or_404(Porduct,slug)
      try:
         instance = Porduct.objects.get(slug=slug,active=True) #for using single product
      except Porduct.DoesNotExist:
         raise Http404("Slug Field ! no product found baby !")
      except Porduct.MultipleObjectsReturned:
         qs = Porduct.objects.filter(slug = slug,active=True)
         instance= qs.first()
      except:
         raise Http404("nothing to show !")

      return instance





"""#################function based view###########################"""

#6
def FB_productListView(request):
   queryset = Porduct.objects.all()
   context = {
      'object_list':queryset
   }
   return render(request,'function_bsed_view/Fb_list.html',context)




#6
# def FB_ProductDetailview(request,*args,**kwargs):
#    #print(args)
#    #instance = Porduct.objects.get(pk=kwargs['pk'])
#    instance = get_object_or_404(Porduct,pk=kwargs['pk'])#if we dont find the product
#    # print(instance.description)
#    # print(kwargs['pk'])
#    context ={
#       'object':instance
#    }
#    return render(request,'function_bsed_view/FB_detail.html',context)



#9
#customize error _1
#error
# def FB_ProductDetailview(request,*args,**kwargs):
#    try:
#       instance = Porduct.objects.get(id=kwargs['pk'])
#    except Porduct.DoesNotExist:
#
#       print("no Product found!")
#       #raise Http404("Custom ! error ! nO product Found")
#
#    except:
#       print('nothing to show')
#    # not_found = "no Product found! "
#
#    context ={
#       'object':instance,
#    }
#    return render(request,'function_bsed_view/FB_detail.html',context)
#

#9
# custom error 2
#error
# def FB_ProductDetailview(request,*args,**kwargs):
#
#    query_set = Porduct.objects.filter(id = kwargs['pk'])
#    if query_set.exists() and query_set.count() == 1:
#       instance = query_set.first()
#    else:
#       raise Http404("Custom ! error ! nO product Found")
#    context ={
#       'object':instance,
#    }
#    return render(request,'function_bsed_view/FB_detail.html',context)
#
#
# #10
#manager
#custom manager

def FB_ProductDetailview(request,*args,**kwargs):
   instance = Porduct.objects.get_by_id(kwargs['pk'])

   if instance is None:
      raise Http404("Custom ! error ! nO product Found")

   context ={
      'object':instance,
   }
   return render(request,'function_bsed_view/FB_detail.html',context)
