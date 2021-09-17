from django.http import Http404
from django.shortcuts import render, get_object_or_404
from products.models import Porduct


def productList(request):
   queryset = Porduct.objects.all()

   context = {
      'object_list':queryset
   }
   return render(request,'product_list_functionBasedView.html',context)



"""----------------------------------product detail-------------------------------                        """

# def productdetail(request,pk):
#    #queryset = Porduct.objects.get(pk=pk)
#    instance = get_object_or_404(Porduct,pk=pk)
#    print(instance.title)
#
#    context = {
#       'object': instance
#    }
#    return render(request,'detail_view_funsctionBasssed.html',context)


#9 look ups
#error handeling

#--------------------------try block
# def productdetail(request,pk):
#    #queryset = Porduct.objects.get(pk=pk)
#    #instance = get_object_or_404(Porduct,pk=pk)
#    #print(instance.title)
#    try:
#       instance = Porduct.objects.get(id=pk)
#    except Porduct.DoesNotExist:
#       print("no product here")
#       #this massage will show in error
#       raise Http404("product dosenot exist")
#    except:
#       print("none")
#    context = {
#       'object': instance
#    }
#    return render(request,'detail_view_funsctionBasssed.html',context)



#-------------filter vs get ----------- data
# def productdetail(request,pk):
#    try:
#       instance = Porduct.objects.get(id=pk)
#       query_set = Porduct.objects.filter(id=pk)
#    except:
#       instance = []
#       query_set = []
#
#
#    context = {
#       'object_instance': instance,
#       'object_qs':query_set
#    }
#    return render(request,'filter_vs_get.html',context)

#--------------using- count and exists specifiy the perameter

# def productdetail(request,pk):
#
#    query_set = Porduct.objects.filter(id=pk)
#
#    if query_set.exists() and query_set.count() == 1:
         #the query set now convert into instance
#       instance = query_set.first()
#    else:
#       raise Http404("product dosent exists")
#
#    context = {
#       'object':instance
#    }
#    return render(request,'detail_view_funsctionBasssed.html',context)


#10
#Model Manager
#retrive data using model Manager
# def productdetail(request,pk):
#
#    query_set = Porduct.objects.filter(id=pk)
#    #inst
#
#    #the query must be conatin value 1
#    if query_set.exists() and query_set.count() == 1:
#       instance = query_set.first()
#    else:
#       raise Http404("product dosent exists")
#
#    context = {
#       'object':instance
#    }
#    return render(request,'detail_view_funsctionBasssed.html',context)


"""as we define  every thing on our model manager
   so we need just call the modified manager object from our excect model """


def productdetail(request,pk):

   instance = Porduct.objects.get_by_id(id=pk)

   if instance is None:
      #creating an error !
      raise Http404("product dosent exists")



   context = {
      'object':instance
   }
   return render(request,'detail_view_funsctionBasssed.html',context)
