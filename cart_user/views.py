from django.shortcuts import render
from cart_user.models import Cart

# Create your views here.





#
# def create_cart():
#    cart_obj = Cart.objects.create(user=None)
#    print('new cart has created')
#    return cart_obj


def cart_view(request):
   #7.4
   #session
   #cart
   #getting cart id using session


   # cart_id = request.session.get("cart_id",None)
   # qs= Cart.objects.filter(id=cart_id)
   # if qs.count() == 1:
   #    print('card ID exists')
   #    cart_obj = qs.first()
   #    if request.user.is_authenticated and cart_obj.user is None:
   #       cart_obj.user = request.user
   #       cart_obj.save()
   # else:
   #    cart_obj = Cart.objects.new(user=request.user)
   #    request.session['cart_id'] = cart_obj.id

   #7.7
   #define all method in model manager

   cart_obj,new_obj = Cart.objects.new_or_get(request)
   print(cart_obj)
   print(new_obj)
   return render(request,'cart_view.html')


