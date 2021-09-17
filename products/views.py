from django.shortcuts import render,get_object_or_404

from .models import Porduct

# Create your views here.






def productList(request):
   queryset = Porduct.objects.all()

   context = {
      'object_list':queryset
   }
   return render(request,'product_list_functionBasedView.html',context)







def productdetail(request,pk):
   #queryset = Porduct.objects.get(pk=pk)
   instance = get_object_or_404(Porduct,pk=pk)
   print(instance.title)

   context = {
      'object': instance
   }
   return render(request,'detail_view_funsctionBasssed.html',context)
