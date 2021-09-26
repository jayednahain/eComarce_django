from django.db import models
#from cart_user.models import Cart
from cart_user.models import Cart

class CartManager(models.Manager):

   #7.7
   def new_or_get(self,request):
      cart_id = request.session.get("cart_id", None)
      # qs = Cart.objects.filter(id=cart_id)
      qs = self.get_queryset().filter(id=cart_id)
      if qs.count() == 1:
         #new
         new_obj= False
         print('card ID exists')
         cart_obj = qs.first()
         if request.user.is_authenticated and cart_obj.user is None:
            cart_obj.user = request.user
            cart_obj.save()
      else:
         cart_obj = Cart.objects.new(user=request.user)
         #new
         new_obj =True
         request.session['cart_id'] = cart_obj.id
      return cart_obj,new_obj



   def new(self,user=None):
      print(user.is_authenticated)
      user_obj = None
      if user is not None:
         if user.is_authenticated:
            user_obj=user
         else:
            print("user is not authenticated")
      return self.model.objects.create(user=user_obj)
