from django.db import models

#9
#image path
from products.media_path_converter import upload_image_path
from products.manager import ProductManager
#12
#signal
from django.db.models.signals import pre_save,post_save

#12
#slug generator function
from products.slug_generator import unique_slug_generator
from django.urls import reverse
from django.db import models
from django.db.models import Q



#11 7:45
#creating custmon queryset model!





class Porduct(models.Model):
   title          = models.CharField(max_length=120)
   description    = models.TextField()
   price          = models.DecimalField(decimal_places=2,max_digits=20,default=00.00)
   product_image  = models.ImageField(upload_to=upload_image_path,null=True,blank=True)

   #coustom manager
   objects         = ProductManager()

   #11
   featured       = models.BooleanField(default=False)

   #12
   active         = models.BooleanField(default=True)
   slug           = models.SlugField(blank=True,unique=True)
   date           = models.DateTimeField(auto_now_add=True)


   def __str__(self):
      return str(self.title)

   def slug_product_link(self):
      return reverse("CB_slug_deatil",kwargs={"slug":self.slug})

   # def get_absolute_url(self):
   #    return "/product/product_slug_detail_CB/{slug}/".format(slug=self.slug)

#12
#signal
#this signal will create when any one create any product
#this signal will generate slug !
def product_pre_save_reciver(sender,instance,*args,**kwargs):
   if not instance.slug:
      instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_reciver,sender=Porduct)